from django.shortcuts import render
from models import Grupo
from .models import Publicacion
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def listarPosts(request):
	pubs = Publicacion.objects.order_by('fecha_publicacion')
	grupos = Grupo.objects.order_by('fecha_inicio')
	return render(request, 'index.html', {'pubs' : pubs, 'grupos' : grupos})

def grupos(request, pk):
	grupo = Grupo.objects.filter(pk = pk).order_by('nombre_grupo')
	return render(request, 'clubfans.html', {'grupo' : grupo})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			publicacion = form.save(commit=False)
			publicacion.autor = request.user
			publicacion.fecha_publicacion = timezone.now()
			publicacion.save()
			return render(request, 'post_edit.html', {'form': form})
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})