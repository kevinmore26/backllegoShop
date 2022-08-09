# Generated by Django 3.2.7 on 2022-08-09 03:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='clienteModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('clienteId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('clienteNombre', models.CharField(db_column='nombre', max_length=50, verbose_name='Nombre del usuario')),
                ('clienteApellido', models.CharField(db_column='apellido', max_length=50, verbose_name='Apellido del usuario')),
                ('clienteCorreo', models.EmailField(db_column='email', max_length=50, unique=True)),
                ('clienteDireccion', models.CharField(db_column='direccion', max_length=50, null=True, verbose_name='Dirección del usuario')),
                ('clienteTipo', models.IntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'MIEMBRO'), (3, 'CLIENTE')], db_column='tipo', default=3)),
                ('clienteDocumento', models.CharField(db_column='documento', max_length=9, null=True)),
                ('clienteCelular', models.IntegerField(db_column='celular', null=True)),
                ('password', models.TextField(null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='PerfilModel',
            fields=[
                ('perfilId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('perfilNick', models.CharField(db_column='nick', max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('productoId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('productoNombre', models.CharField(db_column='nombre', max_length=50, verbose_name='nombre')),
                ('productoPrecio', models.DecimalField(db_column='precio', decimal_places=2, max_digits=9, verbose_name='precio')),
                ('productoDescripcion', models.CharField(db_column='descripcion', max_length=100, verbose_name='descripcion')),
                ('productoFoto', models.ImageField(db_column='foto', null=True, upload_to='productos/')),
                ('productoCantidad', models.IntegerField(db_column='cantidad', default=0)),
                ('productoDisponible', models.BooleanField(db_column='disponible', default=True)),
                ('updatedAt', models.DateField(auto_now=True, db_column='updated_at')),
                ('createdAt', models.DateField(auto_now_add=True, db_column='created_at')),
                ('productoTipo', models.CharField(choices=[('1', 'comidaRapida'), ('2', 'miniMarket'), ('3', 'supermercado')], db_column='productoTipo', default='1', max_length=10)),
                ('productoSubTipo', models.CharField(db_column='productoSubTipo', default='kfc', max_length=10)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'productos',
                'ordering': ['-productoPrecio'],
            },
        ),
        migrations.CreateModel(
            name='PedidoModel',
            fields=[
                ('pedidoId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('pedidoFecha', models.DateField(auto_now_add=True, db_column='fecha')),
                ('pedidoTotal', models.DecimalField(db_column='total', decimal_places=2, max_digits=9)),
                ('cliente', models.ForeignKey(db_column='cliente_id', on_delete=django.db.models.deletion.PROTECT, related_name='clientePedidos', to='gestion.clientemodel')),
                ('vendedor', models.ForeignKey(db_column='vendedor_id', on_delete=django.db.models.deletion.PROTECT, related_name='vendedorPedidos', to='gestion.clientemodel')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoModel',
            fields=[
                ('detalleId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('detalleCantidad', models.IntegerField(db_column='cantidad', validators=[django.core.validators.MinValueValidator(0, 'Valor no puede ser negativo')])),
                ('detalleSubTotal', models.DecimalField(db_column='sub_total', decimal_places=2, max_digits=9)),
                ('pedido', models.ForeignKey(db_column='pedido_id', on_delete=django.db.models.deletion.PROTECT, related_name='pedidoDetalles', to='gestion.pedidomodel')),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.PROTECT, related_name='productoDetalles', to='gestion.productomodel')),
            ],
            options={
                'db_table': 'detalles',
            },
        ),
        migrations.CreateModel(
            name='AdopcionModel',
            fields=[
                ('adopcionId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('adopcionNombre', models.CharField(db_column='nombre', max_length=14)),
                ('adopcionEdad', models.IntegerField(db_column='edad', null=True)),
                ('adopcionTamanio', models.TextField(choices=[('P', 'PEQUEÑO'), ('M', 'MEDIANO'), ('G', 'GRANDE')], db_column='tamanio', default='M')),
                ('adopcionCaracteristicas', models.CharField(db_column='caracteristicas', max_length=100)),
                ('adopcionFoto', models.ImageField(db_column='foto', null=True, upload_to='adopciones/')),
                ('adopcionEstado', models.BooleanField(db_column='estado', default=True)),
                ('cliente', models.ForeignKey(blank=True, db_column='cliente_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clienteAdopcion', to='gestion.clientemodel')),
            ],
            options={
                'verbose_name': 'adopcion',
                'verbose_name_plural': 'adopciones',
                'db_table': 'adopciones',
                'ordering': ['-adopcionTamanio'],
            },
        ),
    ]
