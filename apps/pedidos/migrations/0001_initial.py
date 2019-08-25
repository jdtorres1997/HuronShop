# Generated by Django 2.2.4 on 2019-08-22 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '__first__'),
        ('clientes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutivo', models.IntegerField(default=0)),
                ('no_pedido', models.CharField(max_length=20, verbose_name='Numero de pedido')),
                ('direccion', models.CharField(max_length=75, verbose_name='Dirección de entrega')),
                ('fecha_entrega', models.DateField(verbose_name='Fecha de entrega')),
                ('total_compra', models.IntegerField(null=True)),
                ('estado_pedido', models.CharField(choices=[('', ''), ('En proceso', 'En proceso'), ('Listo', 'Listo'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado')], default='', max_length=10)),
                ('estado_pago', models.CharField(choices=[('', ''), ('No pagado', 'No pagado'), ('Pagado', 'Pagado')], default='', max_length=10)),
                ('cliente', models.ForeignKey(limit_choices_to={'alive': True}, on_delete=django.db.models.deletion.PROTECT, related_name='clientes', related_query_name='cliente', to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='MvtoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('costo', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('talla', models.CharField(choices=[('', ''), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L')], default='', max_length=2)),
                ('color', models.CharField(default='', max_length=50, verbose_name='Color')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', related_query_name='pedido', to='pedidos.Pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productos', related_query_name='producto', to='productos.Producto')),
            ],
        ),
    ]
