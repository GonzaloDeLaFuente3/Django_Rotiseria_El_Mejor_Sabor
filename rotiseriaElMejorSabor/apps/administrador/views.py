from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
from .forms import PedidoForm
# # Create your views here.
# def index(request):
#     return HttpResponse('hola mundo')
from .models import Pedido


def admin_login(request):
    return  render(request, 'administrador/admin-login.html')

def administrador_configuracion(request):
    return  render(request, 'administrador/configuracion-admin.html')



def estadisticas(request):
    return  render(request, 'administrador/estadisticas.html')

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
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario


    return render(request, 'administrador/pedido.html', data)