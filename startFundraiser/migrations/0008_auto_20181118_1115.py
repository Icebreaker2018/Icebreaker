# Generated by Django 2.1.1 on 2018-11-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0007_auto_20181118_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
