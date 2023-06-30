import ast
import json

from django.db import models


class Champion(models.Model):
    # Keys below are dropped from API
    # intro, lane, tags, searchkey
    heroId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=200)
    avatar = models.URLField()
    card = models.URLField()
    poster = models.URLField()
    highlightprice = models.IntegerField()
    couponprice = models.IntegerField()
    isWeekFree = models.BooleanField()
    difficultyL = models.IntegerField()
    damage = models.IntegerField()
    surviveL = models.IntegerField()
    assistL = models.IntegerField()

    def __str__(self):
        return self.name

    def set_roles(self, x):
        self.roles = json.dumps(x)

    def get_roles(self):
        return ast.literal_eval(self.roles)


class ChampionStatistic(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    hero_id = models.IntegerField()
    strength = models.IntegerField()
    weight = models.IntegerField()
    appear_rate = models.FloatField()
    appear_bzc = models.IntegerField()
    forbid_rate = models.FloatField()
    forbid_bzc = models.IntegerField()
    win_rate = models.FloatField()
    win_bzc = models.IntegerField()
    dtstatdate = models.DateField()
    strength_level = models.IntegerField()
    league = models.CharField(max_length=20)
    lane = models.CharField(max_length=20)

    def __str__(self):
        return self.id
