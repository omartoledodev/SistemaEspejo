# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanciones', '0003_auto_20150115_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sancion',
            name='concepto',
            field=models.ForeignKey(to='csanciones.ConceptoSancion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sancion',
            name='empleado',
            field=models.ForeignKey(to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
    ]
