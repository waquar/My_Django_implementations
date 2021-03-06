# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0002_auto_20180219_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indexapp.Bank')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
