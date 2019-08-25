# Generated by Django 2.2.4 on 2019-08-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='El nombre de la linea no puede estar vacio ni sobre pasar el limite de 75 carcteres', max_length=75, unique=True, verbose_name='Nombre de la linea:')),
                ('description', models.TextField(blank=True, verbose_name='Descripción de la linea:')),
                ('active', models.BooleanField(default=True, help_text='Desiga si la Linea se encuentra activa en el sistema')),
            ],
        ),
    ]
