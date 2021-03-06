# Generated by Django 2.0.3 on 2018-04-16 20:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20180415_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_article_like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='user_article_like',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 22, 59, 48, 629619)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 22, 59, 48, 630100)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 22, 59, 48, 630601)),
        ),
        migrations.DeleteModel(
            name='User_article_like',
        ),
        migrations.AddField(
            model_name='voter',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Article'),
        ),
        migrations.AddField(
            model_name='voter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
