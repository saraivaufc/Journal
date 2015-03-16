# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_remove_offer_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalist',
            options={'verbose_name': 'Journalist', 'verbose_name_plural': 'Journalists', 'permissions': (('registering_news', 'Registering News'), ('delete_news', 'Delete News'))},
        ),
        migrations.AlterModelOptions(
            name='lector',
            options={'verbose_name': 'Lector', 'verbose_name_plural': 'Lectors', 'permissions': (('registering_lector', 'Registering Lector'), ('comment_news', 'Comment News'), ('offer_to_buy', 'Offer to Buy'))},
        ),
        migrations.AlterModelOptions(
            name='redator',
            options={'verbose_name': 'Redator', 'verbose_name_plural': 'Redators', 'permissions': (('registering_journalist', 'Registering Journalist'), ('registering_classifield', 'Registering Classifield'), ('registering_section', 'Registering Section'), ('registering_subsection', 'Registering SubSection'), ('delete_news', 'Delete News'))},
        ),
    ]
