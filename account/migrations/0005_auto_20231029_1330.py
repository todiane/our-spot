# Generated by Django 3.2.22 on 2023-10-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_auto_20231028_2303"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("follower", models.CharField(max_length=1000)),
                ("user", models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="profile",
            name="following",
        ),
    ]
