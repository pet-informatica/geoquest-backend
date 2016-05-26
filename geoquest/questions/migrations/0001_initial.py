# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-26 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('is_correct', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('exam', models.CharField(max_length=100, verbose_name='Exam')),
                ('option_a', models.CharField(max_length=500, verbose_name='Option A')),
                ('option_b', models.CharField(max_length=500, verbose_name='Option B')),
                ('option_c', models.CharField(max_length=500, verbose_name='Option C')),
                ('option_d', models.CharField(max_length=500, verbose_name='Option D')),
                ('option_e', models.CharField(max_length=500, verbose_name='Option E')),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('level', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='Level')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Category')),
            ],
        ),
        migrations.AddField(
            model_name='badge',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Category'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]