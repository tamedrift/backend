import requests

from wildrift_cn.models import ChampionStatistic


def process_stats(stats: dict) -> list[ChampionStatistic]:
    models = []
    for league, lanes in stats["data"].items():
        for lane, champions in lanes.items():
            for champion in champions:
                champion["league"] = league
                champion["lane"] = lane
                model = ChampionStatistic(**champion)
                models.append(model)
    return models


def run():
    url = "https://mlol.qt.qq.com/go/lgame_battle_info/hero_rank_list_v2"
    res = requests.get(url)
    stats = res.json()

    models = process_stats(stats)

    ChampionStatistic.objects.bulk_create(models)
