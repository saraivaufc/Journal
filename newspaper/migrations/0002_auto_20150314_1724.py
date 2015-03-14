# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifield',
            name='phone',
            field=models.IntegerField(max_length=10, verbose_name='Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message='Length has to be 10', code='Invalid number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='phone',
            field=models.IntegerField(max_length=10, verbose_name='Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message='Length has to be 10', code='Invalid number')]),
            preserve_default=True,
        ),
    ]
