from django import forms
from .models import Publicacion
from .models import Grupo

class PostForm(forms.ModelForm):

	class Meta:
		model = Publicacion
		fields = ('titulo', 'contenido',)

class GrupoForm(forms.ModelForm):

	class Meta:
		model = Grupo
		fields = ('nombre_grupo',)
			