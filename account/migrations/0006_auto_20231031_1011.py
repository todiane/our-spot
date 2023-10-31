# Generated by Django 3.2.22 on 2023-10-31 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20231029_1330'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
