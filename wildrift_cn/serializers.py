from rest_framework import serializers

from wildrift_cn.models import Champion, TierList


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ["heroId", "name", "roles", "avatar"]


class TierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TierList
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
