from django.http import HttpResponse
from django.core import serializers
from wildrift_cn.models import ChampionStatistic


def statistics(request):
    stats = ChampionStatistic.objects.all()
    sstats = serializers.serialize('json', stats)
    return HttpResponse(sstats, content_type="application/json")
