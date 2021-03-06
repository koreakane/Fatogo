# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-20 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0002_auto_20181220_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyreview',
            name='avgScore',
            field=models.CharField(default='testasdas', max_length=3),
        ),
        migrations.AddField(
            model_name='companyreview',
            name='reviewedDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='companyreview',
            name='reviewedGroup',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AddField(
            model_name='companyreview',
            name='reviewedText',
            field=models.TextField(default='testasdas', max_length=2000),
        ),
        migrations.AlterField(
            model_name='companyaccounts',
            name='authority',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaccounts',
            name='password',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaccounts',
            name='tid',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address1',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address2',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address3',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address4',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address5',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address5_1',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address6',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address6_1',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address7',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='address8',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='addressLatitude',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaroundenvironment',
            name='EnvironmentExplain',
            field=models.TextField(default='testasdas', max_length=20000),
        ),
        migrations.AlterField(
            model_name='companyaroundenvironment',
            name='EnvironmentName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyaroundfacilites',
            name='facilitesExplain',
            field=models.TextField(default='testasdas', max_length=20000),
        ),
        migrations.AlterField(
            model_name='companyaroundfacilites',
            name='facilitesName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyauxiliaryfacilites',
            name='facilitesName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyinfomations',
            name='hotelName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyinnerroomfacilites',
            name='facilitesName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companymasterinfomations',
            name='masterBusinessLicenseNumber',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companymasterinfomations',
            name='masterEmail',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companymasterinfomations',
            name='masterName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companymasterinfomations',
            name='masterPhoneNumber',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='companymasterinfomations',
            name='masterRegistrationNumber',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='desiredTripAreaGU',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='desiredTripAreaGUUN',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='desiredTripAreaSI',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='organizationName',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='startingAreaGU',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='startingAreaGUUN',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='startingAreaSI',
            field=models.CharField(default='testasdas', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tripPerpose',
            field=models.CharField(default='testasdas', max_length=100),
        ),
    ]
