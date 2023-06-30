import requests

from wildrift_cn.catalog import catalog
from wildrift_cn.models import Champion


def get_champions() -> dict[str, str]:
    url = "https://game.gtimg.cn/images/lgamem/act/lrlib/js/heroList/hero_list.js"
    champs = requests.get(url)
    return champs.json()


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
    start_index = url.rfind("/") + 1  # Find the index of the last "/"
    end_index = url.rfind("_")  # Find the index of the last "_"
    champion_name = url[start_index:end_index]
    return champion_name


def run():
    champs = get_champions()
    models = process_champions(champs)
    Champion.objects.bulk_create(models)
