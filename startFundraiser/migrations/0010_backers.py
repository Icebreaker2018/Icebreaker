# Generated by Django 2.1.1 on 2018-11-18 08:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0009_campaign_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backer', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('date_backed', models.DateTimeField(default=django.utils.timezone.now)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startFundraiser.Campaign')),
            ],
        ),
    ]