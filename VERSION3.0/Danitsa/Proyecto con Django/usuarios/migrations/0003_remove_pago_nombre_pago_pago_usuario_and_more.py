# Generated by Django 4.1.2 on 2023-06-21 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_fecha_nacimiento_usuario_form_birthday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='nombre_pago',
        ),
        migrations.AddField(
            model_name='pago',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_pagos', to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='metodo_pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios_metodopago', to='usuarios.pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.IntegerField(choices=[(1, 'Mastercard'), (2, 'Visa'), (3, 'American Express')]),
        ),
    ]
