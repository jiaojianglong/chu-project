# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='photo',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
