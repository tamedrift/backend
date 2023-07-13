from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wildrift_cn import views

urlpatterns = [
    path(
        "champion_statistics",
        views.ChampionStatisticsList.as_view(),
        name="champion_statistics",
    ),
    path("champions", views.ChampionsList.as_view(), name="champions"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
