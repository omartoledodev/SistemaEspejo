# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='email',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='idusuario',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='clave_evento',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
