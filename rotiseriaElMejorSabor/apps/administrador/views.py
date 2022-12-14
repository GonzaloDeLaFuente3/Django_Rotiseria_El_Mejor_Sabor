from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .forms import PedidoForm
# # Create your views here.
# def index(request):
#     return HttpResponse('hola mundo')
from .models import Pedido
from ..cadete.models import Cadete


@permission_required('administrador.view_pedido', login_url="navegacion:login")
def admin_login(request):
    pedidos = Pedido.objects.all()
    data = {
        'pedidos': pedidos
    }
    return  render(request, 'administrador/admin-login.html', data)

@permission_required('administrador.view_pedido', login_url="navegacion:login")
def estado_pedido(request):
    pedidos = Pedido.objects.all()
    data = {
        'pedidos': pedidos
    }
    return render(request, 'administrador/modificarEstadoPedido.html', data)


@permission_required('administrador.change_pedido', login_url="navegacion:login")
def editar_estado_pedido(request, id):
    print(id)
    pedido = Pedido.objects.get(id=id)

    data={
        'pedido': pedido
    }
    if request.method == 'POST':
        estadoPedido = request.POST['estadoPedido']
        pedido.estadoPedido = estadoPedido
        pedido.save()
        print("guardado")
        return redirect(reverse("administrador:estado_pedido"))
    return render(request, 'administrador/editarEstadoPedido.html', data )


@permission_required('administrador.view_pedido', login_url="navegacion:login")
def administrador_configuracion(request):
    return  render(request, 'administrador/configuracion-admin.html')

@permission_required('administrador.view_pedido', login_url="navegacion:login")
def estadistica_principal(request):
    cadetes = Cadete.objects.all()
    data = {
        'cadeteOpciones':cadetes
    }
    return render(request, 'administrador/estadisticas.html', data)

@permission_required('administrador.view_pedido', login_url="navegacion:login")
def estadisticas(request):
    cuil = request.POST['cuilCadete']
    cadete = Cadete.objects.get(cuil=cuil)
    pedidoCadete = Pedido.objects.filter(cadete=cadete)
    cadetes = Cadete.objects.all()
    data = {
        'pedidos': pedidoCadete,
        'cadete': cadete,
        'cadeteOpciones': cadetes
    }

    messages.success(request, "se mostrara los pedidos enviados por el cadete seleccionado")
    return  render(request, 'administrador/estadisticas.html', data)




@permission_required('administrador.view_pedido', login_url="navegacion:login")
def consulta_fecha(request):
    fechaConsulta = request.POST['fechaPedido']
    print(fechaConsulta)
    pedidoConsultaFecha = Pedido.objects.filter(fechaPedido = fechaConsulta)
    cadetes = Cadete.objects.all()
    data = {
        'cadeteOpciones': cadetes,
        'pedidosFechas': pedidoConsultaFecha
    }
    messages.success(request, "se mostrara los pedido con la fecha ingresada")
    return render(request, 'administrador/estadisticas.html', data)

@permission_required('administrador.view_pedido', login_url="navegacion:login")
def historial_pedidos(request):
    pedidos = Pedido.objects.all()
    data = {
        'pedidos': pedidos
    }


    return  render(request, 'administrador/historial-pedidos.html', data)

# def ver_empleados(request):
#     return  render(request, 'administrador/verEmpleados.html')

@permission_required('administrador.add_pedido', login_url="navegacion:login")
def registrar_pedido(request):
    data = {
        'form': PedidoForm()
    }
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se Agrego un pedido nuevo correctamente")
        else:
            data["form"] = formulario


    return render(request, 'administrador/pedido.html', data)

@permission_required('administrador.change_pedido', login_url="navegacion:login")
def modificar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    data = {
        'form': PedidoForm(instance=pedido),
        'id': id

    }
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido)
        print("antes if")
        if formulario.is_valid():
            formulario.save()
            print("se guardo")
            messages.success(request, "Se modifico correctamente")
            return redirect(reverse("administrador:admin_login"))
        data["form"] = formulario
    return render(request, 'administrador/modificarPedido.html', data )

