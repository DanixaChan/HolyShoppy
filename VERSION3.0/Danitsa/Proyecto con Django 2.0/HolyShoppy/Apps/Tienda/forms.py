from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Usuario,Detalleproducto,Pago,Producto

class UsuarioForm(ModelForm):
    class Meta:
        model=Usuario
        fields=['form_user' ,'form_password' ,'form_correo' ,'form_direction' ,'form_birthday']
        exclude=['id_usuario', 'imagen','fecha_venta']

