# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20171210_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
