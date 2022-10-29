# Generated by Django 4.1.2 on 2022-10-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('tipoMenu', models.IntegerField(choices=[(1, 'Entrada'), (2, 'Plato principal'), (3, 'Postre')])),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vigencia', models.BooleanField(default=False)),
                ('tipoComida', models.IntegerField(choices=[(1, 'Normal'), (2, 'Vegetariano'), (3, 'Celiaco'), (4, 'Diabetico')])),
                ('imagen', models.CharField(max_length=600, unique=True)),
            ],
        ),
    ]
