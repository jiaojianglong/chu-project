# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20170412_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='time',
            field=models.CharField(max_length=32),
        ),
    ]
