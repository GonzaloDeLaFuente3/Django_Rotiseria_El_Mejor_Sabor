from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import lower
from apps.cadete.models import Cadete
from django.contrib import messages
# Create your views here.
@permission_required('empleado.add_empleado', login_url="navegacion:login")
def cadete_login(request):
    return render(request, 'cadete/cadete-login.html')

@permission_required('empleado.change_empleado', login_url="navegacion:login")
def configuracion_cadete(request):
    return render(request, 'cadete/configuracion-cadete.html')

@permission_required('empleado.change_empleado', login_url="navegacion:login")
def modificarCadete(request):
    return  render(request, 'cadete/modificarCadete.html')

@permission_required('empleado.delete_empleado', login_url="navegacion:login")
def eliminarCadete(request,cuil):
    cadete = Cadete.objects.get(cuil=cuil)
    cadete.delete()
    #redireccion
    messages.success(request, "se elimino el cadete correctamente")
    return redirect(reverse("empleado:ver"))

@permission_required('empleado.change_empleado', login_url="navegacion:login")
def modificarCadete(request, cuil):
    return  render(request, 'cadete/modificarCadete.html', {'cadete': Cadete.objects.get(cuil=cuil)})

@permission_required('empleado.change_empleado', login_url="navegacion:login")
def editarCadete(request):
    cuil = request.POST['cuil']
    nombre = lower(request.POST['nombre'])
    apellido = lower(request.POST['apellido'])
    domicilio_calle = lower(request.POST['domicilio_calle'])
    domicilio_numero = request.POST['domicilio_numero']
    domicilio_localidad = lower(request.POST['domicilio_localidad'])
    domicilio_departamento = lower(request.POST['domicilio_departamento'])
    vigenciaCarnet = request.POST['vigenciaCarnet']
    codigoZona = request.POST['codigoZona']
    patente = request.POST['patente']

    telefonoFijo = request.POST['telefonoFijo']
    telefonoCelular = request.POST['telefonoCelular']
    fechaNacimiento = request.POST['fechaNacimiento']
    fechaIngreso = request.POST['fechaIngreso']

    cadete = Cadete.objects.get(cuil=cuil)
    cadete.nombre = nombre
    cadete.apellido = apellido
    cadete.domicilio_localidad = domicilio_localidad
    cadete.domicilio_departamento = domicilio_departamento
    cadete.fechaIngreso = fechaIngreso
    cadete.fechaNacimiento = fechaNacimiento
    cadete.domicilio_calle = domicilio_calle
    cadete.domicilio_numero = domicilio_numero
    cadete.telefonoFijo = telefonoFijo
    cadete.telefonoCelular = telefonoCelular
    cadete.patente = patente
    cadete.vigenciaCarnet = vigenciaCarnet
    cadete.codigoZona = codigoZona

    cadete.save()
    messages.success(request, "se modifico el cadete correctamente")
    return redirect(reverse("empleado:ver"))