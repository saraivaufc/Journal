# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_auto_20150320_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
    ]
