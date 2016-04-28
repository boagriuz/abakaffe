# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('update', '0003_remove_coffeebrewer_brews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('RFID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='update.CoffeeBrewer')),
            ],
        ),
    ]
