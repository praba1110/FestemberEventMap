# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0005_auto_20160910_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stall',
            name='slug',
        ),
    ]
