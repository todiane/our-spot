# Generated by Django 3.2.22 on 2023-10-24 17:20

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[300, 300],
                upload_to="account/",
            ),
        ),
    ]
