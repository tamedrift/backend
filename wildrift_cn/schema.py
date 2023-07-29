from datetime import date
from typing import Optional

from ninja import FilterSchema, ModelSchema

from wildrift_cn.models import Champion, ChampionStatistic


class TierListFilterSchema(FilterSchema):
    league: Optional[int]
    lane: Optional[int]
    dtstatdate: Optional[date]


class TierListOut(ModelSchema):
    class Config:
        model = ChampionStatistic
        model_fields = [
            "hero_id",
            "appear_rate",
            "appear_bzc",
            "forbid_rate",
            "forbid_bzc",
            "win_rate",
            "win_bzc",
            "tier",
            "win_pct",
            "appear_pct",
            "forbid_pct",
        ]


class ChampionOut(ModelSchema):
    class Config:
        model = Champion
        model_fields = [
            "heroId",
            "name",
            "roles",
            "avatar",
        ]
