from django.db.models import Max
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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


@method_decorator(cache_page(timeout=60 * 15), name="dispatch")
class LastDateView(APIView):
    def get(self, request, format=None):
        # Retrieve the maximum 'dtstatdate' using Django ORM aggregation
        last_date = TierList.objects.aggregate(max_date=Max("dtstatdate"))["max_date"]

        # Return the result in the response
        return Response({"last_date": last_date})
