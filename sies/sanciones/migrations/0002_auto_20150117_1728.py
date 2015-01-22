# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sancion',
            old_name='fecha',
            new_name='fecha_s',
        ),
        migrations.RenameField(
            model_name='sancion',
            old_name='gafete',
            new_name='gafete_s',
        ),
        migrations.RenameField(
            model_name='sancion',
            old_name='idevento',
            new_name='idevento_s',
        ),
    ]
