# Generated by Django 4.1.2 on 2023-07-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_remove_producto_nombreca_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='nombreCa_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
