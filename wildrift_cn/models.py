import json
from django.db import models


class Hero(models.Model):
    heroId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
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
        return json.loads(self.roles)


class HeroStatistic(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.id

