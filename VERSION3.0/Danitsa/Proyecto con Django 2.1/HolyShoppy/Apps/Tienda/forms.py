from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Usuario,Detalleproducto,Pago,Producto

class UsuarioForm(ModelForm):
    form_payment_card = forms.ModelChoiceField(queryset=Pago.objects.all(), to_field_name='form_payment_card')
    class Meta:
        model=Usuario
        fields=['form_user' ,'form_password' ,'form_correo' ,'form_direction' ,'form_birthday','form_payment_card']
        exclude=['id_usuario', 'imagen','fecha_venta']

