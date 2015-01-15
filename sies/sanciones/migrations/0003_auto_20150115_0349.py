# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csanciones', '0001_initial'),
        ('sanciones', '0002_auto_20150115_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sancion',
            name='sancion',
        ),
        migrations.AddField(
            model_name='sancion',
            name='concepto',
            field=models.OneToOneField(default=2, to='csanciones.ConceptoSancion'),
            preserve_default=False,
        ),
    ]
