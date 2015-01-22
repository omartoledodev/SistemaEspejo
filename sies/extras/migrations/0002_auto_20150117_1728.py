# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extra',
            old_name='cantidad',
            new_name='cantidad_e',
        ),
        migrations.RenameField(
            model_name='extra',
            old_name='fecha',
            new_name='fecha_e',
        ),
        migrations.RenameField(
            model_name='extra',
            old_name='gafete',
            new_name='gafete_e',
        ),
    ]
