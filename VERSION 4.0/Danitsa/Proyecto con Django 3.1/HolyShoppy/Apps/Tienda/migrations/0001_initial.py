# Generated by Django 4.1.2 on 2023-07-02 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('nombreCa_id', models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(default='Categoria por defecto', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Detalleproducto',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(db_column='idPago', primary_key=True, serialize=False)),
                ('form_payment_card', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default=None, max_length=70)),
                ('precio', models.PositiveBigIntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('descripcion', models.TextField(default='Descripción por defecto', max_length=350)),
                ('stock', models.PositiveBigIntegerField(default=0)),
                ('nombreCa_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Tienda.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('form_user', models.CharField(max_length=20)),
                ('form_password', models.CharField(max_length=20)),
                ('form_correo', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('form_direction', models.CharField(blank=True, max_length=50, null=True)),
                ('form_birthday', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='usuarios')),
                ('fecha_venta', models.ManyToManyField(through='Tienda.Detalleproducto', to='Tienda.producto')),
                ('form_payment_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.pago')),
            ],
        ),
        migrations.AddField(
            model_name='detalleproducto',
            name='id_pago',
            field=models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='Tienda.pago'),
        ),
        migrations.AddField(
            model_name='detalleproducto',
            name='id_producto',
            field=models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='Tienda.producto'),
        ),
        migrations.AddField(
            model_name='detalleproducto',
            name='id_usuario',
            field=models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario'),
        ),
    ]