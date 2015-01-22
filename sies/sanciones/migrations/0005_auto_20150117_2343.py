# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanciones', '0004_auto_20150117_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sancion',
            old_name='idevento_s',
            new_name='cantidad_s',
        ),
    ]
