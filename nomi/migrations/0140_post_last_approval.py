# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0139_post_elder_brother'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_approval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last', to='nomi.Post'),
        ),
    ]
