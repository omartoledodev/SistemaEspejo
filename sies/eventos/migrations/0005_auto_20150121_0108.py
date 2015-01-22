# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_evento_verificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='verificado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
