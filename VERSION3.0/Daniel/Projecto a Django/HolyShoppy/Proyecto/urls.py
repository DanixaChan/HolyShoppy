from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informaciones', views.informaciones, name='informaciones'),
    path('Categorias', views.pagCategorias, name='Categorias'),
    path('detallemicro1', views.detallemicro1, name='detallemicro1'),
    path('promocion', views.promocion, name='promocion'),
    path('registro', views.registro, name='registro'),
    path('Electrodomesticos', views.Electrodomesticos, name='Electrodomesticos'),
    path('carro', views.carro, name='carro'),
    path('gestionProductos', views.gestionProductos, name='gestionProductos'),
    path('registrarProducto/', views.registrarProducto),
    path('editarProducto/<id_producto>', views.editarProducto, name='editarProducto'),
    path('edicionProducto/', views.edicionProducto, name='edicionProducto'),
    path('eliminarProducto/<id_producto>', views.eliminarProducto, name='eliminarProducto'),
]