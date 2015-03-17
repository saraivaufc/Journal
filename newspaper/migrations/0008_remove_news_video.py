# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0007_news_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='video',
        ),
    ]
