# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-30 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20180830_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
