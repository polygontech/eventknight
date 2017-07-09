# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_hash', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tw_user', models.CharField(max_length=200)),
                ('tw_user_token', models.CharField(max_length=400)),
                ('tw_user_token_secret', models.CharField(max_length=400)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='live_event.Event')),
            ],
        ),
    ]
