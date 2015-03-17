# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0009_news_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalist',
            options={'verbose_name': 'Journalist', 'verbose_name_plural': 'Journalists', 'permissions': (('registering_news', 'Registering News'), ('view_news', 'View News'), ('delete_news', 'Delete News'))},
        ),
    ]
