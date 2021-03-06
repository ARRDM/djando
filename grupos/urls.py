from django.conf.urls import url
from . import views

# Listado de url's para los grupos.
urlpatterns = [
	url(r'^$', views.listarPosts, name='listarPosts'),
	url(r'(?P<pk>\d+)/$', views.grupos, name='grupos'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^grupo/new/$', views.grupo_new, name='grupo_new'),
	url(r'^usuario/new/$', views.usuario_new, name="usuario_new"),
	url(r'^login/$', views.iniciarsesion, name='iniciarsesion')
]