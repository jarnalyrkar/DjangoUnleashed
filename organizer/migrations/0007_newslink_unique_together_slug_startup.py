# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'startup')]),
            ),
    ]