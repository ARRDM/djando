from django import forms
from .models import Publicacion
from .models import Grupo
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model = Publicacion
		fields = ('titulo', 'contenido',)

class GrupoForm(forms.ModelForm):

	class Meta:
		model = Grupo
		fields = ('nombre_grupo',)

class RegistroForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class InicioSesionForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)