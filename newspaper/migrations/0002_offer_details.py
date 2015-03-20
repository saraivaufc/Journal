# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='details',
            field=models.TextField(null=True, verbose_name='Details', blank=True),
            preserve_default=True,
        ),
    ]
