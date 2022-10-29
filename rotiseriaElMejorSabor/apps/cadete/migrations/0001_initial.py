# Generated by Django 4.1.2 on 2022-10-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadete',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empleado.empleado')),
                ('vigenciaCarnet', models.DateField()),
                ('patente', models.CharField(max_length=7, unique=True)),
                ('codigoZona', models.IntegerField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('empleado.empleado',),
        ),
    ]
