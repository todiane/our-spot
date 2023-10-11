# Generated by Django 3.2.22 on 2023-10-11 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='locations/')),
                ('image_alt', models.CharField(max_length=100)),
                ('location_types', models.CharField(choices=[('africa', 'Africa'), ('america', 'America'), ('asia', 'Asia'), ('caribbean', 'Caribbean'), ('europe', 'Europe'), ('great_britain', 'Great Britain'), ('middle_east', 'Middle East')], default='Africa', max_length=50)),
                ('posted_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_date'],
            },
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
    ]
