# Generated by Django 4.1.2 on 2023-06-25 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_rename_metodo_pago_pago_form_payment_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='form_payment_card',
            field=models.ForeignKey(db_column='formPaymentCard', null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.pago'),
        ),
    ]
