from django.contrib import admin
from .models import Publicacion
from .models import Grupo

# Register your models here.
admin.site.register(Publicacion)
admin.site.register(Grupo)