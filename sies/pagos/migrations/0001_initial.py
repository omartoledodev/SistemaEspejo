# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empleado', models.CharField(max_length=200)),
                ('asistencias', models.PositiveIntegerField()),
                ('inasistencias', models.PositiveIntegerField()),
                ('extras', models.PositiveIntegerField()),
                ('sanciones', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
