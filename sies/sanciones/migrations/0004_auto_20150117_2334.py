# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanciones', '0003_auto_20150117_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sancion',
            name='fecha_s',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
