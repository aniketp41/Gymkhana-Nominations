# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-06 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0131_auto_20170806_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='nomi_session',
            field=models.IntegerField(null=True),
        ),
    ]