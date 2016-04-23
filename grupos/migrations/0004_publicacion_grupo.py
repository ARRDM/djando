# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0003_auto_20160423_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='grupo',
            field=models.ForeignKey(default=0, to='grupos.Grupo'),
            preserve_default=False,
        ),
    ]
