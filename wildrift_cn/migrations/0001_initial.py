# Generated by Django 4.2.2 on 2023-07-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Champion",
            fields=[
                ("heroId", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("roles", models.CharField(max_length=200)),
                ("avatar", models.URLField()),
                ("card", models.URLField()),
                ("poster", models.URLField()),
                ("highlightprice", models.IntegerField()),
                ("couponprice", models.IntegerField()),
                ("isWeekFree", models.BooleanField()),
                ("difficultyL", models.IntegerField()),
                ("damage", models.IntegerField()),
                ("surviveL", models.IntegerField()),
                ("assistL", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ChampionStatistic",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("position", models.IntegerField()),
                ("hero_id", models.IntegerField()),
                ("strength", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("appear_rate", models.DecimalField(decimal_places=4, max_digits=5)),
                ("appear_bzc", models.IntegerField()),
                ("forbid_rate", models.DecimalField(decimal_places=4, max_digits=5)),
                ("forbid_bzc", models.IntegerField()),
                ("win_rate", models.DecimalField(decimal_places=4, max_digits=5)),
                ("win_bzc", models.IntegerField()),
                ("dtstatdate", models.DateField()),
                ("strength_level", models.IntegerField()),
                ("league", models.IntegerField()),
                ("lane", models.IntegerField()),
                ("tier", models.IntegerField()),
            ],
            options={
                "ordering": ["win_bzc"],
            },
        ),
    ]
