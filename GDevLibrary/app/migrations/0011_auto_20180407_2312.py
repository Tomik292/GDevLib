# Generated by Django 2.0.3 on 2018-04-07 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180402_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='points',
        ),
        migrations.AlterField(
            model_name='article',
            name='overview',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 23, 12, 19, 647330)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 23, 12, 19, 647830)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 23, 12, 19, 648331)),
        ),
    ]
