# Generated by Django 4.0.1 on 2022-01-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemgame',
            name='step',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]