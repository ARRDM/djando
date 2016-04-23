from django.shortcuts import render
from models import Grupo
from .models import Publicacion
from django.utils import timezone

# Create your views here.
def listarPosts(request):
	pubs = Publicacion.objects.order_by('fecha_publicacion')
	return render(request, 'index.html', {'pubs' : pubs})