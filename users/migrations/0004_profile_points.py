# Generated by Django 4.0.1 on 2022-01-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_arm_l_profile_arm_r_profile_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
