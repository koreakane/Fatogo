# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-22 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0008_companyaddress_addresslongitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymasterinfomations',
            name='companyInfo_CompanyMasterInfomationsFK',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
    ]
