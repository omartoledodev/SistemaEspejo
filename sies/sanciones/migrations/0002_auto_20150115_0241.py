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
            old_name='genero',
            new_name='sancion',
        ),
    ]
