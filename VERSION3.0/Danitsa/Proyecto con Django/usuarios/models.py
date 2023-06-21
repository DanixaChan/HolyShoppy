from django.db import models



class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    descripcion_producto = models.CharField(max_length=350)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return str(self.nombre_producto)
    
class Detalleproducto(models.Model):
    id_detalle = models.AutoField(db_column='idDetalle', primary_key=True)
    fecha_venta = models.DateField(blank=False, null=False) 
    id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE, db_column='idProducto')  
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, db_column='idUsuario')  
 
    def __str__(self):
        return str(self.fecha_venta)

class Pago(models.Model):
    id_pago = models.AutoField(db_column='idPago', primary_key=True)
    METODO_PAGO_CHOICES = (
        ('mastercard', 'Mastercard'),
        ('visa', 'Visa'),
        ('amex', 'American Express'),
    )
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='usuario_pagos', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.metodo_pago)


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='idUsuario', primary_key=True)
    form_user = models.CharField(max_length=20)
    form_password = models.CharField(max_length=20)
    form_correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    form_direction = models.CharField(max_length=50, blank=True, null=True)
    form_birthday = models.DateField(blank=False, null=False)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    metodo_pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios_metodopago')

    def __str__(self):
        return self.form_user        
""" class Usuario(models.Model):
    id_usuario       = models.AutoField(db_column='idUsuario', primary_key=True)
    form_user           = models.CharField(max_length=20)
    form_password       = models.CharField(max_length=20)
    form_correo            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    form_direction        = models.CharField(max_length=50, blank=True, null=True)  
    form_birthday = models.DateField(blank=False, null=False) 
    imagen           = models.ImageField(upload_to="usuarios", null=True)
    #id_pago tiene problemas, Pago esta despues :/
    id_pago = models.ForeignKey(Pago, on_delete=models.SET_DEFAULT, default=1, related_name='usuarios_idpago')
    metodo_pago = models.ForeignKey('Pago', on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios_metodopago')

    def __str__(self):
        return self.form_user  
    
class Pago(models.Model):
    id_pago = models.AutoField(db_column='idPago', primary_key=True)
    METODO_PAGO_CHOICES = (
            (1, 'Mastercard'),
            (2, 'Visa'),
            (3, 'American Express'),
        )
    metodo_pago = models.IntegerField(choices=METODO_PAGO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_pagos')
    def __str__(self):
        return str(self.metodo_pago) """
# Create your models here.
