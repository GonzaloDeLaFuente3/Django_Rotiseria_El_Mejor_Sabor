# Generated by Django 4.1.2 on 2022-10-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.CharField(max_length=11, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('domicilio_calle', models.CharField(max_length=200)),
                ('domicilio_numero', models.IntegerField()),
                ('domicilio_localidad', models.CharField(max_length=250)),
                ('domicilio_barrio', models.CharField(max_length=200)),
                ('domicilio_observacion', models.TextField(blank=True)),
                ('domicilio_zona', models.CharField(choices=[('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste')], max_length=5)),
                ('telefono', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]