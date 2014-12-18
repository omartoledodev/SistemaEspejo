# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('clave', models.AutoField(serialize=False, verbose_name=b'Clave', primary_key=True)),
                ('evento', models.CharField(max_length=200)),
                ('teatro', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('hombres', models.PositiveIntegerField()),
                ('mujeres', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
