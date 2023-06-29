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

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.UsuarioAdd, name='registro'),
    path('UsuarioDelete/<str:form_user>', views.UsuarioDelete, name='UsuarioDelete'),
    path('edicionUsuario/<str:form_user>', views.edicionUsuario, name='edicionUsuario'),
    path('UsuarioEdit/<str:form_user>/', views.UsuarioEdit, name='UsuarioEdit'),
    path('listUser/', views.listUser, name='listUser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
