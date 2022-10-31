from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import lower
from django.urls import reverse
from apps.empleado.models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages

def altaEmpleado(request):
    return render(request,'empleado/altaEmpleado.html')

def bajaCadete(request):
    return  render(request, 'empleado/bajaCadete.html')

def modificarCadete(request):
    return  render(request, 'empleado/modificarCadete.html')

def verEmpleados(request):
    return  render(request, 'empleado/verEmpleados.html')

def registrar_empleado(request):
    data = {
        'form': EmpleadoForm()
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'empleado/altaEmpleados.html', data)