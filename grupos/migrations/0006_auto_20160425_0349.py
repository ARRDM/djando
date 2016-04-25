# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20160423_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo', blank=True),
        ),
    ]
