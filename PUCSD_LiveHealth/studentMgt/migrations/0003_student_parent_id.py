# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-16 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentMgt', '0002_auto_20180815_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='studentMgt.Parent'),
            preserve_default=False,
        ),
    ]
