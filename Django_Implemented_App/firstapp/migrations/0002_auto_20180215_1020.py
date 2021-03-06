# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pincode', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AlterModelTable(
            name='college',
            table='college',
        ),
    ]
