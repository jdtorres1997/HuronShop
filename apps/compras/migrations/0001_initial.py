# Generated by Django 2.2.4 on 2019-08-22 22:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='El nombre de la linea no puede estar vacio ni sobre pasar el limite de 75 carcteres', max_length=75, unique=True, verbose_name='Nombre del producto a comprar:')),
                ('descripcion', models.TextField(blank=True, verbose_name='Motivo de compra:')),
                ('estado_compra', models.CharField(choices=[('En proceso', 'En proceso'), ('Pago', 'Pago')], default='', max_length=10)),
                ('precio', models.IntegerField(default=0, help_text='Ingrsa el precio individual de cada producto', verbose_name=django.core.validators.MinValueValidator(0, 'El valor minimo de una compra no puede ser menor a 0'))),
                ('cantidad', models.IntegerField(default=0, verbose_name=django.core.validators.MinValueValidator(0, 'Debes comprar al menos un producto'))),
                ('precio_total', models.IntegerField(default=0, verbose_name=django.core.validators.MinValueValidator(0, 'El valor minimo de una compra no puede ser menor a 0'))),
            ],
        ),
    ]
