from django.contrib import admin
from .models import Producto, Categorias

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categorias)