# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-19 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True, verbose_name='updated at')),
                ('raw_value', models.TextField(verbose_name='value')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('kind', models.CharField(choices=[('int', 'integer'), ('str', 'text'), ('time', 'time'), ('date', 'date'), ('json', 'json')], max_length=255, verbose_name='kind')),
                ('cache_seconds', models.PositiveIntegerField(default=3600, verbose_name='cache seconds')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]