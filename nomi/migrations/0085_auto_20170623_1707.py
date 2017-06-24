# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0084_groupnomination_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupnomination',
            name='creator',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_holders',
            field=models.ManyToManyField(blank=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]