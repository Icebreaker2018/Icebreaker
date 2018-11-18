# Generated by Django 2.1.1 on 2018-11-18 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('startFundraiser', '0005_auto_20181118_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('camp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='startFundraiser.Campaign')),
            ],
        ),
    ]
