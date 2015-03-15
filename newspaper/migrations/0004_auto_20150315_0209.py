# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_auto_20150314_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['-value'], 'verbose_name': 'Offer', 'verbose_name_plural': 'Offers'},
        ),
        migrations.AlterField(
            model_name='classifield',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Phone'),
            preserve_default=True,
        ),
    ]
