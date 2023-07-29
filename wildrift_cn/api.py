from ninja import Query, Router

from wildrift_cn.models import Champion, ChampionStatistic
from wildrift_cn.schema import ChampionOut, TierListFilterSchema, TierListOut

router = Router()


@router.get("/tier_list", response=list[TierListOut])
def tier_list(request, filters: TierListFilterSchema = Query(...)):
    q = filters.get_filter_expression()
    return ChampionStatistic.objects.filter(q)


@router.get("/champions/{champion_id}", response=ChampionOut)
def champion(request, champion_id: int):
    return Champion.objects.filter(heroId=champion_id).first()


@router.get("/champions", response=list[ChampionOut])
def champions(request):
    return Champion.objects.all()
