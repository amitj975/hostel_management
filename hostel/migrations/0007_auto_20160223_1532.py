# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_auto_20160223_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='room_no',
            new_name='room',
        ),
    ]
