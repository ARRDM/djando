from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.listarPosts, name='listarPosts'),
	url(r'(?P<pk>\d+)/$', views.grupos, name='grupos'),
	url(r'^post/new/$', views.post_new, name='post_new'),
]