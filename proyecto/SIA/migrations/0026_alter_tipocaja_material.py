# Generated by Django 5.1 on 2024-11-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIA', '0025_alter_vehiculo_marca_alter_vehiculo_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocaja',
            name='Material',
            field=models.CharField(choices=[('carton', 'Cartón'), ('madera', 'Madera')], max_length=20),
        ),
    ]
