# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0041_auto_20170605_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can approve the post', 'can approve the post'), ('can send nominations to users', 'can send nominations to users'))},
        ),
        migrations.AlterField(
            model_name='nomination',
            name='dept_choice',
            field=models.CharField(choices=[('All', 'All'), ('Aerospace Engineering', 'AE'), ('Biological Sciences & Engineering', 'BSBE'), ('Chemical Engineering', 'CHE'), ('Civil Engineering', 'CE'), ('Computer Science & Engineering', 'CSE'), ('Electrical Engineering', 'EE'), ('Materials Science & Engineering', 'MSE'), ('Mechanical Engineering', 'ME'), ('Industrial & Management Engineering', 'IME'), ('Chemistry', 'CHM'), ('Mathematics & Scientific Computing', 'MTH'), ('Physics', 'PHY'), ('Earth Sciences', 'ES')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='hall_choice',
            field=models.CharField(choices=[('All', 'All'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='year_choice',
            field=models.CharField(choices=[('All', 'All'), ('Y16', 'Y16'), ('Y15', 'Y15'), ('Y14', 'Y14'), ('Y13', 'Y13'), ('Y12', 'Y12'), ('Y11', 'Y11')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Post created', 'Post created'), ('Post approved', 'Post approved'), ('Post rejected', 'Post rejected'), ('Post on work', 'Post on work')], default='Post created', max_length=50),
        ),
    ]
