# Generated by Django 2.2.4 on 2019-08-22 22:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lineas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('nombre', models.CharField(max_length=75, verbose_name='Nombre del producto:')),
                ('etiquetas', models.TextField(blank=True, help_text='Añade aqui las etiquetas que estan relacionadas con tu producto', verbose_name='Etiquetas relacionadas con el producto')),
                ('precio', models.IntegerField(help_text='Define un valor de venta para este producto', verbose_name=django.core.validators.MinValueValidator(0, 'El valor minimo de un producto no puede ser menor a 0'))),
                ('tallas', multiselectfield.db.fields.MultiSelectField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L')], help_text='Selecciona todas las opciones de tallas en las cuales este producto estara disponible', max_length=50)),
                ('linea', models.ForeignKey(limit_choices_to={'active': True}, on_delete=django.db.models.deletion.PROTECT, related_name='lineas', related_query_name='linea', to='Lineas.Linea')),
            ],
        ),
    ]
