# Generated by Django 2.1.1 on 2018-11-08 19:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181105_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 8, 19, 31, 3, 576239, tzinfo=utc), null=True),
        ),
    ]
