# Generated by Django 4.2.3 on 2023-08-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wildrift_cn", "0003_rename_championstatistic_tierlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="champion",
            name="heroId",
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]