# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20160928_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media'),
        ),
    ]
