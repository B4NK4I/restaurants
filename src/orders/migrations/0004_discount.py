# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180706_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(default=0)),
                ('key', models.CharField(blank=True, default='', max_length=100)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]
