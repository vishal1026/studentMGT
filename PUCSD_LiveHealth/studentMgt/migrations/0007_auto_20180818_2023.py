# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-18 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentMgt', '0006_auto_20180818_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_in_class',
            name='roll_no',
            field=models.IntegerField(default=1),
        ),
    ]
