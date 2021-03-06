# Generated by Django 2.0.3 on 2018-04-14 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180407_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 21, 1, 5, 608062)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 21, 1, 5, 608562)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 21, 1, 5, 609062)),
        ),
    ]
