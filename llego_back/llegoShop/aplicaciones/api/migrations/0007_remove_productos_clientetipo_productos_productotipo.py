# Generated by Django 4.0.4 on 2022-07-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_productos_clientetipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='clienteTipo',
        ),
        migrations.AddField(
            model_name='productos',
            name='productoTipo',
            field=models.CharField(choices=[('1', 'comidaRapida'), ('2', 'miniMarket'), ('3', 'supermercado')], default='1', max_length=10),
        ),
    ]
