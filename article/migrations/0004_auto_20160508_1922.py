# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160508_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='\u6240\u5c5e\u677f\u5757'),
        ),
    ]