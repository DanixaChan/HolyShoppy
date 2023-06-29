from django.db import models


class Categorias(models.Model): 
    nombre_categoria = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    precio = models.PositiveBigIntegerField()
    nombreCa = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.TextField()
    stock = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nombre