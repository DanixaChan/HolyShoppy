from django.contrib import admin
from .models import Usuario,Pago,Detalleproducto,Producto,Categorias

admin.site.register(Usuario)
admin.site.register(Pago)
admin.site.register(Detalleproducto)
admin.site.register(Producto)
admin.site.register(Categorias)
