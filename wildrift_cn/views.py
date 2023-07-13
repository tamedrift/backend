from rest_framework import generics

from wildrift_cn.models import Champion, ChampionStatistic
from wildrift_cn.serializers import ChampionSerializer, ChampionStatisticSerializer


class ChampionStatisticsList(generics.ListCreateAPIView):
    queryset = ChampionStatistic.objects.all()
    serializer_class = ChampionStatisticSerializer


class ChampionsList(generics.ListCreateAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
