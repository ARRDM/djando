from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Clase para
class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length=255)
	fecha_inicio = models.DateTimeField()

	def get_absolute_url(self):
		return "/people/%i/" % self.id

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

class Publicacion(models.Model):
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
	autor = models.ForeignKey('auth.User', null=True, blank=True)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_publicacion = models.DateTimeField(default=timezone.now)