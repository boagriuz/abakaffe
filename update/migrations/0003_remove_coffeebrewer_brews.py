# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeebrewer',
            name='brews',
        ),
    ]