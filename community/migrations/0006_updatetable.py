# Generated by Django 2.1.2 on 2018-11-18 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_commenttable_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.CharField(max_length=1000)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.GroupTable')),
            ],
        ),
    ]
