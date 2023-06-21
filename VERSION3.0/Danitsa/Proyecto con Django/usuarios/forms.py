from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Usuario,Producto,Pago

class UsuarioForm(ModelForm):

    class Meta:
        model=Usuario
        #fields="__all__"
        fields=['form_user' ,'form_password' ,'form_correo' ,'form_direction' ,'form_birthday']
        exclude = ['id_usuario', 'imagen']
        widgets={'fecha_nacimiento':forms.SelectDateWidget}
        metodo_pago = forms.ChoiceField(choices=Pago.METODO_PAGO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

class ProductoForm(ModelForm):

    class Meta:
        model=Producto
        #fields="__all__"
        fields=['id_producto','nombre_producto','descripcion_producto','precio_producto','imagen_producto']

class RegistroForm(UserCreationForm):
    metodo_pago = forms.ChoiceField(choices=Pago.METODO_PAGO_CHOICES)

    class Meta:
        model = Usuario
        fields = ('form_user', 'form_password', 'form_correo', 'form_direction', 'form_birthday', 'metodo_pago')
