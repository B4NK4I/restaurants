# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20180707_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='expected_date',
        ),
    ]
