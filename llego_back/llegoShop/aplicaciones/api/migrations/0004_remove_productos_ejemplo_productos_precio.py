# Generated by Django 4.0.4 on 2022-06-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_productos_ejemplo_alter_productos_stockproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='ejemplo',
        ),
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.CharField(default='0', max_length=10),
        ),
    ]