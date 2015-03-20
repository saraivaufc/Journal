# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_auto_20150320_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='details',
            field=models.TextField(default=datetime.datetime.now, null=True, verbose_name='Details', blank=True),
            preserve_default=True,
        ),
    ]
