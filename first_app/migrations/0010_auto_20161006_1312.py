# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_auto_20161006_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
    ]