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


class TierList(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    position = models.IntegerField()
    hero_id = models.IntegerField()
    strength = models.IntegerField()
    weight = models.IntegerField()
    appear_rate = models.DecimalField(max_digits=5, decimal_places=4)
    appear_bzc = models.IntegerField()
    forbid_rate = models.DecimalField(max_digits=5, decimal_places=4)
    forbid_bzc = models.IntegerField()
    win_rate = models.DecimalField(max_digits=5, decimal_places=4)
    win_bzc = models.IntegerField()
    dtstatdate = models.DateField()
    strength_level = models.IntegerField()
    league = models.IntegerField()
    lane = models.IntegerField()
    tier = models.IntegerField()
    win_pct = models.IntegerField()
    appear_pct = models.IntegerField()
    forbid_pct = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["win_bzc"]
