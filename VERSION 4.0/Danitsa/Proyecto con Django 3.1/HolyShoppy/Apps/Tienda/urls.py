"""
URL configuration for HolyShoppy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.UsuarioAdd, name='registro'),
    path('UsuarioDelete/<str:form_user>', views.UsuarioDelete, name='UsuarioDelete'),
    path('edicionUsuario/<str:form_user>', views.edicionUsuario, name='edicionUsuario'),
    path('UsuarioEdit/<str:form_user>/', views.UsuarioEdit, name='UsuarioEdit'),
    path('listUser/', views.listUser, name='listUser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)