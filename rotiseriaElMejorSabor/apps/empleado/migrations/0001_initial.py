# Generated by Django 4.1.2 on 2022-10-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cuil', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('domicilio_localidad', models.CharField(max_length=250)),
                ('domicilio_calle', models.CharField(max_length=250)),
                ('domicilio_numero', models.IntegerField()),
                ('telefonoFijo', models.IntegerField(null=True)),
                ('telefonoCelular', models.IntegerField()),
                ('domicilio_departamento', models.CharField(max_length=300)),
                ('fechaNacimiento', models.DateField()),
                ('fechaIngreso', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
