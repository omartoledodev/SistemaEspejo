# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cextras', '0001_initial'),
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='extra',
        ),
        migrations.AddField(
            model_name='extra',
            name='concepto',
            field=models.OneToOneField(default=2, to='cextras.ConceptoExtra'),
            preserve_default=False,
        ),
    ]
