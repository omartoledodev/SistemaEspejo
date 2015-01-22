# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='fecha',
            new_name='fecha_a',
        ),
        migrations.RenameField(
            model_name='asistencia',
            old_name='gafete',
            new_name='gafete_a',
        ),
        migrations.RenameField(
            model_name='asistencia',
            old_name='idevento',
            new_name='idevento_a',
        ),
    ]
