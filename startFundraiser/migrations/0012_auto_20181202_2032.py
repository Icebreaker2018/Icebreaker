# Generated by Django 2.0.5 on 2018-12-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0011_auto_20181118_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='end_Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_Date',
            field=models.DateTimeField(),
        ),
    ]
