# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_auto_20150115_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='concepto',
            field=models.ForeignKey(to='cextras.ConceptoExtra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extra',
            name='empleado',
            field=models.ForeignKey(to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
    ]
