# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0118_auto_20170805_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tenure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomi.Session'),
        ),
    ]
