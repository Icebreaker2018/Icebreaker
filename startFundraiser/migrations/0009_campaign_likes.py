# Generated by Django 2.1.1 on 2018-11-18 07:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('startFundraiser', '0008_auto_20181118_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
