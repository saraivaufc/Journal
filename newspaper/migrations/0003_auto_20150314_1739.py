# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_auto_20150314_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifield',
            name='offers',
            field=models.ManyToManyField(to='newspaper.Offer', null=True, verbose_name='Offers', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classifield',
            name='phone',
            field=models.IntegerField(max_length=10, verbose_name='Phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='phone',
            field=models.IntegerField(max_length=10, verbose_name='Phone'),
            preserve_default=True,
        ),
    ]
