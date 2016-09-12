# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stall',
            options={'ordering': ('stallName',)},
        ),
        migrations.RemoveField(
            model_name='stall',
            name='stall_description',
        ),
        migrations.RemoveField(
            model_name='stall',
            name='stall_name',
        ),
        migrations.AddField(
            model_name='stall',
            name='slug',
            field=models.SlugField(default=b'-1', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='stall',
            name='stallDescription',
            field=models.CharField(default=b'newDesc', max_length=200),
        ),
        migrations.AddField(
            model_name='stall',
            name='stallLocation',
            field=models.CharField(default=b'newLoc', max_length=250),
        ),
        migrations.AddField(
            model_name='stall',
            name='stallName',
            field=models.CharField(default=b'newStall', max_length=100),
        ),
    ]