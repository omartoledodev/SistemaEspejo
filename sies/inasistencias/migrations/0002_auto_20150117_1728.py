# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inasistencias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inasistencia',
            old_name='fecha',
            new_name='fecha_i',
        ),
        migrations.RenameField(
            model_name='inasistencia',
            old_name='gafete',
            new_name='gafete_i',
        ),
        migrations.RenameField(
            model_name='inasistencia',
            old_name='idevento',
            new_name='idevento_i',
        ),
    ]
