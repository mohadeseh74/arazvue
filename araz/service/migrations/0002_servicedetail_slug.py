# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
