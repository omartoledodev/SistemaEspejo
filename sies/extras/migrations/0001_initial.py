# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0008_auto_20150115_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra', models.PositiveIntegerField()),
                ('empleado', models.OneToOneField(to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
