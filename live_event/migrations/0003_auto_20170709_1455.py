# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('live_event', '0002_auto_20170708_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
