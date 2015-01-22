# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listas_asistencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='gafete_l',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
