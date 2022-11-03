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


def admin_login(request):
    pedidos = Pedido.objects.all()
    data = {
        'pedidos': pedidos
    }
    return  render(request, 'administrador/admin-login.html', data)

def administrador_configuracion(request):
    return  render(request, 'administrador/configuracion-admin.html')

def estadistica_principal(request):
    cadetes = Cadete.objects.all()
    data = {
        'cadeteOpciones':cadetes
    }
    return render(request, 'administrador/estadisticas.html', data)

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

def historial_pedidos(request):
    pedidos = Pedido.objects.all()
    data = {
        'pedidos': pedidos
    }


    return  render(request, 'administrador/historial-pedidos.html', data)

# def ver_empleados(request):
#     return  render(request, 'administrador/verEmpleados.html')

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

