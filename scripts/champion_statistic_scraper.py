import requests
import numpy as np
from wildrift_cn.models import ChampionStatistic


def process_stats(stats: dict, n: int = 5) -> list[ChampionStatistic]:
    models = []
    for league, lanes in stats["data"].items():
        for lane, champions in lanes.items():
            models += process_champions(champions, league, lane)
    return models


def process_champions(champions: list, league: str, lane: str, n: int = 5) -> list[ChampionStatistic]:
    processed_champions = []

    # Splits into 'n' tiers
    sorted_champions = sorted(champions, key=lambda x: int(x['win_bzc']))
    champion_lists = np.array_split(sorted_champions, 5)

    # Process per tier
    for i, champion_list in enumerate(champion_lists):
        for champion in champion_list:
            champion["league"] = league
            champion["lane"] = lane
            champion["tier"] = i + 1
            processed_champion = ChampionStatistic(**champion)
            processed_champions.append(processed_champion)
    return processed_champions


def run():
    url = "https://mlol.qt.qq.com/go/lgame_battle_info/hero_rank_list_v2"
    res = requests.get(url)
    stats = res.json()

    models = process_stats(stats)

    ChampionStatistic.objects.bulk_create(models)
