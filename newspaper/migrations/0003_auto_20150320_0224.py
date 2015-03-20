# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_offer_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anonymous',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Anonymous',
        ),
    ]
