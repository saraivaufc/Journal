# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_auto_20150320_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='Phone Contact', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classifield',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone Contact'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_offer',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Dating Offer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='details',
            field=models.TextField(null=True, verbose_name='Details', blank=True),
            preserve_default=True,
        ),
    ]
