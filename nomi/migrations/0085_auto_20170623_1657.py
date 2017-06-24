# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
        ('nomi', '0084_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='club',
            field=models.ManyToManyField(related_name='club_tags', to='info.ClubTag'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='post',
            field=models.ManyToManyField(related_name='user_post', to='nomi.Post'),
        ),
    ]