from rest_framework import generics

from wildrift_cn.models import Champion, ChampionStatistic
from wildrift_cn.serializers import ChampionSerializer, ChampionStatisticSerializer


class ChampionStatisticsList(generics.ListAPIView):
    queryset = ChampionStatistic.objects.all()
    serializer_class = ChampionStatisticSerializer
    filterset_fields = ["league", "lane"]


class ChampionsList(generics.ListAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer


class ChampionsDetail(generics.RetrieveAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
