# Generated by Django 4.1.2 on 2023-06-23 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_alter_usuario_metodo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='metodo_pago',
            field=models.ForeignKey(db_column='idPago', null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.pago'),
        ),
    ]