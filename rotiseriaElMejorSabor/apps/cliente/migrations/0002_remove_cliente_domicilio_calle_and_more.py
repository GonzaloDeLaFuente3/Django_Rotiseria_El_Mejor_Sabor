# Generated by Django 4.1.2 on 2022-10-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='domicilio_calle',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='domicilio_numero',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cuil',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]