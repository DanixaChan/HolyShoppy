# Generated by Django 4.1.2 on 2023-06-25 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0007_alter_usuario_form_payment_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='form_payment_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.pago'),
        ),
    ]