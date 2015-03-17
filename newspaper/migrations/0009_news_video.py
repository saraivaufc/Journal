# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0008_remove_news_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.FileField(upload_to=b'documents/video/news/%Y/%m/%d', null=True, verbose_name='Video', blank=True),
            preserve_default=True,
        ),
    ]
