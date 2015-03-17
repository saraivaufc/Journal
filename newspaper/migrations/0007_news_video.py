# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0006_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True, verbose_name='Video', blank=True),
            preserve_default=True,
        ),
    ]
