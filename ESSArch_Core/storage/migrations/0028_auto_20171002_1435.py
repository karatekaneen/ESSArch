# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-02 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0027_ioqueue_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessqueue',
            name='aic_xml',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accessqueue',
            name='package_xml',
            field=models.BooleanField(default=False),
        ),
    ]
