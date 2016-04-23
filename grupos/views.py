from django.shortcuts import render
from models import Grupo
from .models import Publicacion
from django.utils import timezone

# Create your views here.
def listarPosts(request):
	pubs = Publicacion.objects.order_by('fecha_publicacion')
	grupos = Grupo.objects.order_by('fecha_inicio')
	return render(request, 'index.html', {'pubs' : pubs, 'grupos' : grupos})