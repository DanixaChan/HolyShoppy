# Generated by Django 4.1.2 on 2023-06-26 21:11

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('precio', models.PositiveBigIntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('descripcion', models.TextField()),
                ('stock', models.PositiveBigIntegerField()),
                ('nombreCa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Proyecto.categorias')),
            ],
        ),
    ]
