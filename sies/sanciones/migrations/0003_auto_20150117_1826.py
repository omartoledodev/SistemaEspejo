# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanciones', '0002_auto_20150117_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sancion',
            name='fecha_s',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
