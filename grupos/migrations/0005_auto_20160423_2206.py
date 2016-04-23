# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0004_publicacion_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
