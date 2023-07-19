from rest_framework import serializers

from wildrift_cn.models import Champion, ChampionStatistic


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ["heroId", "name", "roles", "avatar"]


class ChampionStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionStatistic
        fields = [
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
