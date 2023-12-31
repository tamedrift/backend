import os
import uuid
import logging

import pandas as pd
import requests
from pandera import Check, Column, DataFrameSchema

from wildrift_cn.catalog import catalog
from wildrift_cn.models import Champion, TierList

API = os.environ.get("API_URL", "http://localhost:8000")
SCHEMA = DataFrameSchema(
    {
        "id": Column(int),
        "position": Column(int),
        "hero_id": Column(int, Check.gt(10000)),
        "strength": Column(int),
        "weight": Column(int),
        "appear_rate": Column(float, Check.in_range(0, 1)),
        "appear_bzc": Column(int, Check.gt(0)),
        "forbid_rate": Column(float, Check.in_range(0, 1)),
        "forbid_bzc": Column(int, Check.gt(0)),
        "win_rate": Column(float, Check.in_range(0, 1)),
        "win_bzc": Column(int, Check.gt(0)),
        "dtstatdate": Column(str, Check.str_length(8, 8)),
        "strength_level": Column(int),
        "league": Column(int),
        "lane": Column(int),
    },
    strict=True,
    coerce=True,
)


def create_dataframe_with_features(
    data: list, league: str, lane: str, schema: DataFrameSchema
) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df = df.assign(league=league).assign(lane=lane)
    df = schema.validate(df)

    df = (
        df
        # Create a unique id
        .assign(id=[uuid.uuid4().hex for _ in range(len(df))])
        # Create tier based on the quantiles from win_rate
        .assign(tier=5 - pd.cut(df.win_rate, 5, labels=False))
        # Create percentiles for bar length in Vue
        .assign(win_pct=pd.cut(df.win_rate, 10, labels=False) + 1)
        .assign(appear_pct=pd.cut(df.appear_rate, 5, labels=False) + 1)
        .assign(forbid_pct=pd.cut(df.forbid_rate, 5, labels=False) + 1)
    )
    return df


def dataframe_to_tier_list(dataframe: pd.DataFrame) -> list[TierList]:
    rows = dataframe.to_dict(orient="records")
    return [TierList(**row) for row in rows]


def process_champions(champions: dict) -> list[Champion]:
    keys_to_drop = {"intro", "lane", "tags", "searchkey", "alias", "title"}
    models = []
    for champ in champions["heroList"].values():
        # Drop useless columns
        champ = {k: v for k, v in champ.items() if k not in keys_to_drop}

        # Translate name
        name = champ["name"]
        if name not in catalog.names:
            champ["name"] = name_from_poster_url(champ["poster"])
        else:
            champ["name"] = catalog.names[name]

        # Translate roles
        champ["roles"] = [catalog.roles[role] for role in champ["roles"]]

        model = Champion(**champ)
        models.append(model)

    return models


def name_from_poster_url(url: str) -> str:
    start_index = url.rfind("/") + 1
    end_index = url.rfind("_")
    champion_name = url[start_index:end_index]
    return champion_name


def run():
    # Scrape chinese data
    url = "https://mlol.qt.qq.com/go/lgame_battle_info/hero_rank_list_v2"
    res = requests.get(url)
    stats = res.json()

    # Check dates
    res = requests.get(API + "/api/wildrift_cn/last_date")
    our_last_date = res.json()["last_date"]
    their_last_date = stats["data"]["1"]["1"][1]["dtstatdate"]
    if our_last_date is None or (
        pd.to_datetime(their_last_date) > pd.to_datetime(our_last_date)
    ):
        # Tier list
        logging.info("Scraping new tier list.")
        for league, lanes in stats["data"].items():
            for lane, champions in lanes.items():
                df = create_dataframe_with_features(champions, league, lane, SCHEMA)
                models = dataframe_to_tier_list(df)
                TierList.objects.bulk_create(models)

        # Champions
        logging.info("Looking for new champions.")
        url = "https://game.gtimg.cn/images/lgamem/act/lrlib/js/heroList/hero_list.js"
        res = requests.get(url)
        champs = res.json()
        models = process_champions(champs)
        Champion.objects.bulk_create(models, ignore_conflicts=True)

    logging.info("No new data available.")
