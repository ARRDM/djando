# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0006_auto_20160425_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo', null=True),
        ),
    ]
