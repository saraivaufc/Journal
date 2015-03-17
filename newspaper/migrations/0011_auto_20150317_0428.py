# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0010_auto_20150317_0357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalist',
            options={'verbose_name': 'Journalist', 'verbose_name_plural': 'Journalists', 'permissions': (('keep_news', 'Keep News'),)},
        ),
        migrations.AlterModelOptions(
            name='redator',
            options={'verbose_name': 'Redator', 'verbose_name_plural': 'Redators', 'permissions': (('keep_journalist', 'Keep Journalist'), ('keep_classifield', 'Keep Classifield'), ('keep_section', 'Keep Section'), ('keep_subsection', 'Keep SubSection'), ('delete_news', 'Delete News'))},
        ),
    ]
