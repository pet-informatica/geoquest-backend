# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-04 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_points'),
        ('users', '0007_auto_20160620_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatistics',
            name='badges',
            field=models.ManyToManyField(to='questions.Badge'),
        ),
    ]
