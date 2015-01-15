# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csanciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptosancion',
            name='cantidad',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
