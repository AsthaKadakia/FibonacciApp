# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0002_auto_20160823_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciparameters',
            name='exec_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fibonacciparameters',
            name='input_parameter',
            field=models.CharField(max_length=100000),
        ),
    ]