# Generated by Django 4.1.2 on 2022-10-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_pedido_fecha_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_hora',
            field=models.TimeField(null=True),
        ),
    ]