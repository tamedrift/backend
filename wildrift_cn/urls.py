from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wildrift_cn import views

urlpatterns = [
    path(
        "tier_list",
        views.TierListView.as_view(),
        name="tier_list",
    ),
    path("champions", views.ChampionsList.as_view(), name="champions"),
    path(
        "champions/<int:pk>", views.ChampionsDetail.as_view(), name="champions_detail"
    ),
    path("last_date", views.LastDateView.as_view(), name="last_date"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
