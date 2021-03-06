from django.shortcuts import render
from models import Grupo
from .models import Publicacion
from django.utils import timezone
from .forms import PostForm
from .forms import GrupoForm
from .forms import RegistroForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
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
			return HttpResponseRedirect("/")
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})

def grupo_new(request):
	if request.method == "POST":
		form = GrupoForm(request.POST)
		if form.is_valid():
			grupo = form.save(commit=False)
			grupo.fecha_inicio = timezone.now()
			grupo.save()
			return HttpResponseRedirect("/")
	else:
		form = GrupoForm()
	return render(request, 'grupo_edit.html', {'form': form})

def usuario_new(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			usuario = form.save(commit=False)
			usuario.save()
			return HttpResponseRedirect("/")
	else:
		form = RegistroForm()
	return render(request, 'usuario_edit.html', {'form': form})

def iniciarsesion(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/")
	return render(request, 'login.html')