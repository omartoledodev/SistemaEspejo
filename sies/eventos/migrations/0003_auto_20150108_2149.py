# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20150107_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='clave',
        ),
        migrations.AddField(
            model_name='evento',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
