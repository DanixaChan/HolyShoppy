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
    id_pago = models.ForeignKey('Pago', on_delete=models.CASCADE, db_column='idPago')
 
    def __str__(self):
        return str(self.fecha_venta)

class Pago(models.Model):
    id_pago = models.AutoField(db_column='idPago', primary_key=True)
    # METODO_PAGO_CHOICES = (
    #     ('mastercard', 'Mastercard'),
    #     ('visa', 'Visa'),
    #     ('amex', 'American Express'),
    # )
    # metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    form_payment_card = models.CharField(max_length=20)
    def __str__(self):
        return str(self.form_payment_card)

class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='idUsuario', primary_key=True)
    form_user = models.CharField(max_length=20)
    form_password = models.CharField(max_length=20)
    form_correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    form_direction = models.CharField(max_length=50, blank=True, null=True)
    form_birthday = models.DateField(blank=False, null=False)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    fecha_venta = models.ManyToManyField(Producto, through=Detalleproducto)
    form_payment_card = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.form_user)
