from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import lower
from django.urls import reverse
from apps.empleado.models import Empleado
from .forms import EmpleadoForm, CadeteForm
from django.contrib import messages



# def bajaCadete(request):
#     return  render(request, 'empleado/bajaCadete.html')
#
# def modificarCadete(request):
#     return  render(request, 'empleado/modificarCadete.html')

def verEmpleados(request):
    return  render(request, 'empleado/verEmpleados.html')

def registrar_empleado(request):
    data = {
        'form_empleado': EmpleadoForm(),
        'form_cadete': CadeteForm()
    }
    if request.method == 'POST':
        formularioEmpleado = EmpleadoForm(data=request.POST)
        formularioCadete = CadeteForm(data=request.POST)

        if formularioEmpleado.is_valid():
            formularioEmpleado.save()
            data["mensaje"] = "guardado correctamente"
            return render(request, 'empleado/altaEmpleado.html', data)
        else:
            data["form_empleado"] = formularioEmpleado

        if formularioCadete.is_valid():
            formularioCadete.save()
            data["mensaje"] = "guardado correctamente"
            return render(request, 'empleado/altaEmpleado.html', data)
        else:
            data["form_cadete"] = formularioCadete

    return render(request, 'empleado/altaEmpleado.html', data)