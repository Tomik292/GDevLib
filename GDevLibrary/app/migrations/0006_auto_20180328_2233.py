# Generated by Django 2.0.3 on 2018-03-28 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180328_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 22, 33, 59, 138546)),
        ),
    ]
