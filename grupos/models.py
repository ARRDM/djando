from django.db import models

class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length=255)
	fecha_inicio = models.DateTimeField()

class Genero(models.Model):
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	nombre_grupo = models.CharField(max_length=50)

class Integrante(models.Model):
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	nombre_integrante = models.CharField(max_length=255)
	apellido_p = models.CharField(max_length=255, blank=True)
	apellido_m = models.CharField(max_length=255, blank=True)

class Album(models.Model):
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	nombre_album = models.CharField(max_length=255)
	anio = models.DateTimeField()