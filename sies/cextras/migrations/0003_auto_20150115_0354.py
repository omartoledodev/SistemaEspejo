# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cextras', '0002_auto_20150115_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptoextra',
            name='cantidad',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
