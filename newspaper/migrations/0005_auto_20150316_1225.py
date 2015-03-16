# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_remove_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dating_comment',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Dating Comment', blank=True),
            preserve_default=True,
        ),
    ]
