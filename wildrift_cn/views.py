from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from wildrift_cn.models import Champion, TierList
from wildrift_cn.serializers import ChampionSerializer, TierListSerializer


@method_decorator(cache_page(timeout=60 * 15), name="dispatch")
class TierListView(generics.ListAPIView):
    queryset = TierList.objects.all()
    serializer_class = TierListSerializer
    filterset_fields = ["league", "lane", "dtstatdate"]
    pagination_class = None


class ChampionsList(generics.ListAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer


@method_decorator(cache_page(timeout=60 * 60 * 30), name="dispatch")
class ChampionsDetail(generics.RetrieveAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
