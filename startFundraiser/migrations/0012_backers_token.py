# Generated by Django 2.0.6 on 2018-12-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0011_auto_20181118_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='backers',
            name='token',
            field=models.CharField(max_length=120, null=True),
        ),
    ]