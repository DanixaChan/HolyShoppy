from django.contrib import admin
from .models import Usuario,Producto,Detalleproducto,Pago

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Detalleproducto)
admin.site.register(Pago)