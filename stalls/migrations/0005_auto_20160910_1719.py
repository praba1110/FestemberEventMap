# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0004_auto_20160910_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall',
            name='slug',
            field=models.SlugField(default=b'0', max_length=20, unique=True),
        ),
    ]
