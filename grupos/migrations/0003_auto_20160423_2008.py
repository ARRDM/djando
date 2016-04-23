# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_auto_20160423_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
