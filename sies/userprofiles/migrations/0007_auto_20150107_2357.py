# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_auto_20150107_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='genero',
            field=models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=True,
        ),
    ]
