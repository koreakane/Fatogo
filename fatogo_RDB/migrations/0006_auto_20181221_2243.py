# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-21 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0005_auto_20181220_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfomations',
            old_name='hotelavgScore',
            new_name='hotelAvgScore',
        ),
    ]