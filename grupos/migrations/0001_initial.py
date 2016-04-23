# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_album', models.CharField(max_length=255)),
                ('anio', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_grupo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_grupo', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_integrante', models.CharField(max_length=255)),
                ('apellido_p', models.CharField(max_length=255, blank=True)),
                ('apellido_m', models.CharField(max_length=255, blank=True)),
                ('grupo', models.ForeignKey(to='grupos.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='genero',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo'),
        ),
        migrations.AddField(
            model_name='album',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo'),
        ),
    ]
