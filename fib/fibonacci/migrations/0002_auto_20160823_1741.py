# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciparameters',
            name='exec_time',
            field=models.CharField(max_length=10000),
        ),
    ]
