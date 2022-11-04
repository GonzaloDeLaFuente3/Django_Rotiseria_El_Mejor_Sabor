from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import lower
from django.urls import reverse
from apps.empleado.models import Empleado
from apps.cadete.models import Cadete
from .forms import EmpleadoForm, CadeteForm
from django.contrib.auth.decorators import permission_required
from django.contrib import messages



@permission_required('empleado.change_empleado', login_url="navegacion:login")
def modificarEmpleado(request):
    return  render(request, 'empleado/modificarEmpleado.html')


@permission_required('empleado.view_empleado', login_url="navegacion:login")
def cargarEmpleados(request):
    return  render(request, 'empleado/verEmpleados.html',
                   {'empleados': Empleado.objects.all(), 'cadetes': Cadete.objects.all()})

@permission_required('empleado.delete_empleado', login_url="navegacion:login")
def eliminarEmpleado(request,cuil):
    empleado = Empleado.objects.get(cuil=cuil)
    empleado.delete()
    #redireccion
    messages.success(request, "se elimino el empleado correctamente")
    return redirect(reverse("empleado:ver"))


#---------------------------------------------------------------------------------
@permission_required('empleado.change_empleado', login_url="navegacion:login")
def modificarEmpleado(request, cuil):
    return  render(request, 'empleado/modificarEmpleado.html', {'empleado': Empleado.objects.get(cuil=cuil)})



@permission_required('empleado.change_empleado', login_url="navegacion:login")
def editarEmpleado(request):
    cuil = request.POST['cuil']
    nombre = lower(request.POST['nombre'])
    apellido = lower(request.POST['apellido'])
    domicilio_calle = lower(request.POST['domicilio_calle'])
    domicilio_numero = request.POST['domicilio_numero']
    domicilio_localidad = lower(request.POST['domicilio_localidad'])
    domicilio_departamento = lower(request.POST['domicilio_departamento'])

    telefonoFijo = request.POST['telefonoFijo']
    telefonoCelular = request.POST['telefonoCelular']
    fechaNacimiento = request.POST['fechaNacimiento']
    fechaIngreso = request.POST['fechaIngreso']

    empleado = Empleado.objects.get(cuil=cuil)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.domicilio_localidad = domicilio_localidad
    empleado.domicilio_departamento= domicilio_departamento
    empleado.fechaIngreso=fechaIngreso
    empleado.fechaNacimiento=fechaNacimiento
    empleado.domicilio_calle=domicilio_calle
    empleado.domicilio_numero=domicilio_numero
    empleado.telefonoFijo = telefonoFijo
    empleado.telefonoCelular = telefonoCelular

    empleado.save()
    messages.success(request, "se modifico el empleado correctamente")
    return redirect(reverse("empleado:ver"))




@permission_required('empleado.add_empleado', login_url="navegacion:login")
def registrar_empleado(request):
    data = {
        'form_empleado': EmpleadoForm(),
        'form_cadete': CadeteForm()
    }

    return render(request, 'empleado/altaEmpleado.html', data)
def registrar_Cadete(request):

    data = {
        'form_cadete': CadeteForm(),
        'form_empleado': EmpleadoForm(),
    }
    if request.method == 'POST':
        formularioCadete = CadeteForm(data=request.POST)
        if formularioCadete.is_valid():
            formularioCadete.save()
            messages.success(request, "Se registro un cadete correctamente")
            return render(request, 'empleado/altaEmpleado.html', data)
        else:

            data["form_cadete"] = formularioCadete
            return render(request, 'empleado/altaEmpleado.html', data)

def registrar_empleado_comun(request):
    data = {
        'form_empleado': EmpleadoForm(),
        'form_cadete': CadeteForm()
    }
    if request.method == 'POST':
        formularioEmpleado = EmpleadoForm(data=request.POST)
        if formularioEmpleado.is_valid():
            formularioEmpleado.save()
            messages.success(request, "Se registro un empleado correctamente")
            return render(request, 'empleado/altaEmpleado.html', data)
        else:
            data["form_empleado"] = formularioEmpleado
            return render(request, 'empleado/altaEmpleado.html', data)