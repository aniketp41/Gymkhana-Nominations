# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0055_auto_20170611_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominationinstance',
            name='comments',
            field=models.CharField(blank=True, default='Interviewer give the comments', max_length=500, null=True),
        ),
    ]
