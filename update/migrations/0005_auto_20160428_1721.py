# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0004_auto_20160428_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeebrewer',
            name='id',
        ),
        migrations.AlterField(
            model_name='coffeebrewer',
            name='RFID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
