from apps.cliente.models import Cliente
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.template.defaultfilters import lower
from django.urls import reverse


@permission_required('cliente.add_cliente', login_url="navegacion:login")
def altaCliente(request):
    cuil = request.POST['cuilCliente']
    nombre = lower(request.POST['nombre'])
    apellido = lower(request.POST['apellido'])
    domicilio_calle = lower(request.POST['calle'])
    domicilio_numero = request.POST['domicilioNumero']
    domicilio_barrio = lower(request.POST['domicilioBarrio'])
    domicilio_localidad = lower(request.POST['localidad'])
    observacion = request.POST['observacion']
    zona = request.POST['codigoZona']
    telefono = request.POST['telefonoCliente']


    cliente = Cliente.objects.create(cuil=cuil, nombre=nombre, apellido=apellido, domicilio_localidad=domicilio_localidad, domicilio_barrio= domicilio_barrio,
                                     domicilio_observacion = observacion, domicilio_zona=zona, telefono=telefono, domicilio_calle=domicilio_calle, domicilio_numero=domicilio_numero )
    messages.success(request, "se registro el cliente correctamente")
    return redirect(reverse("cliente:cargar"))

@permission_required('cliente.change_cliente', login_url="navegacion:login")
def modificarCliente(request):
    return  render(request, 'cliente/modificarCliente.html')


@permission_required('cliente.view_cliente', login_url="navegacion:login")
def cargarClientes(request):
    return render(request, 'cliente/verClientes.html',
                  {'clientes': Cliente.objects.all()})

@permission_required('cliente.delete_cliente', login_url="navegacion:login")
def eliminarCliente(request,cuil):
    cliente = Cliente.objects.get(cuil=cuil)
    cliente.delete()
    #redireccion
    messages.success(request, "se elimino el cliente correctamente")
    return redirect(reverse("cliente:cargar"))

@permission_required('cliente.change_cliente', login_url="navegacion:login")
def modificarCliente(request, cuil):
    return  render(request, 'cliente/modificarCliente.html', {'cliente': Cliente.objects.get(cuil=cuil)})


@permission_required('cliente.change_cliente', login_url="navegacion:login")
def editarCliente(request):
    cuil = request.POST['cuilCliente']
    nombre = lower(request.POST['nombre'])
    apellido = lower(request.POST['apellido'])
    domicilio_calle = lower(request.POST['calle'])
    domicilio_numero = request.POST['domicilioNumero']
    domicilio_barrio = lower(request.POST['domicilioBarrio'])
    domicilio_localidad = lower(request.POST['localidad'])
    observacion = request.POST['observacion']
    zona = request.POST['codigoZona']
    telefono = request.POST['telefonoCliente']



    cliente = Cliente.objects.get(cuil=cuil)
    cliente.nombre = nombre
    cliente.apellido=apellido
    cliente.domicilio_localidad=domicilio_localidad
    cliente.domicilio_barrio= domicilio_barrio
    cliente.domicilio_observacion= observacion
    cliente.domicilio_zona=zona
    cliente.telefono=telefono
    cliente.domicilio_calle=domicilio_calle
    cliente.domicilio_numero=domicilio_numero


    cliente.save()
    messages.success(request, "se modifico el cliente correctamente")
    return redirect(reverse("cliente:cargar"))


def registrar_cliente_desde_index(request):
    cuil = request.POST['cuilCliente']
    nombre = lower(request.POST['nombre'])
    apellido = lower(request.POST['apellido'])
    domicilio_calle = lower(request.POST['calle'])
    domicilio_numero = request.POST['domicilioNumero']
    domicilio_barrio = lower(request.POST['domicilioBarrio'])
    domicilio_localidad = lower(request.POST['localidad'])
    observacion = request.POST['observacion']
    zona = request.POST['codigoZona']
    telefono = request.POST['telefonoCliente']
    print(request.POST['usuario'])
    usuario = request.POST['usuario']

    usuario_baseDatos = User.objects.get(username=usuario)


    cliente = Cliente.objects.create(cuil=cuil, nombre=nombre, apellido=apellido, domicilio_localidad=domicilio_localidad, domicilio_barrio= domicilio_barrio,
                                     domicilio_observacion = observacion, domicilio_zona=zona, telefono=telefono, domicilio_calle=domicilio_calle, domicilio_numero=domicilio_numero, usuario=usuario_baseDatos)
    messages.success(request, "se registro el cliente correctamente")
    return redirect(reverse("index:index"))

    # return render(request, 'cliente/registrarClienteIndex.html')