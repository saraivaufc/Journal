# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_auto_20150315_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(to='newspaper.Comment', null=True, verbose_name='Comments', blank=True),
            preserve_default=True,
        ),
    ]
