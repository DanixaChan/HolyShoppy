# Generated by Django 4.1.2 on 2023-07-02 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='nombreCa_id',
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.categorias'),
        ),
    ]
