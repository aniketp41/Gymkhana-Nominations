# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0020_nominationinstance_filled_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='nomi_form',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Questionnaire'),
        ),
    ]
