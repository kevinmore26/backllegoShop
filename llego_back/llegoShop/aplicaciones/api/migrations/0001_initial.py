# Generated by Django 4.0.4 on 2022-06-12 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('stockProducto', models.PositiveIntegerField(max_length=4)),
                ('productoImagen', models.CharField(max_length=300)),
            ],
        ),
    ]