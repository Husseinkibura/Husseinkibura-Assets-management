# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0006_auto_20160214_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribution',
            old_name='Date',
            new_name='assignment_date',
        ),
    ]
