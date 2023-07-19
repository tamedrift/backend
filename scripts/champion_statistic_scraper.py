import pandas as pd
import requests
from pandera import Check, Column, DataFrameSchema

from wildrift_cn.models import ChampionStatistic

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
        # Create tier based on the quantiles from win_rate
        .assign(tier=5 - pd.cut(df.win_rate, 5, labels=False))
        # Create percentiles for bar length in Vue
        .assign(win_pct=pd.cut(df.win_rate, 10, labels=False) + 1)
        .assign(appear_pct=pd.cut(df.appear_rate, 10, labels=False) + 1)
        .assign(forbid_pct=pd.cut(df.forbid_rate, 10, labels=False) + 1)
    )
    return df


def dataframe_to_champion_statistic(dataframe: pd.DataFrame) -> list[ChampionStatistic]:
    rows = dataframe.to_dict(orient="records")
    return [ChampionStatistic(**row) for row in rows]


def run():
    url = "https://mlol.qt.qq.com/go/lgame_battle_info/hero_rank_list_v2"
    res = requests.get(url)
    stats = res.json()

    for league, lanes in stats["data"].items():
        for lane, champions in lanes.items():
            df = create_dataframe_with_features(champions, league, lane, SCHEMA)
            models = dataframe_to_champion_statistic(df)
            ChampionStatistic.objects.bulk_create(models)
