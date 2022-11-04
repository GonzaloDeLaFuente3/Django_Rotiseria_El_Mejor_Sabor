from django.shortcuts import render

# Create your views here.
from apps.cliente.models import Cliente
from apps.menu.models import Menu
from apps.administrador.models import Pedido
from django.contrib.auth.models import User

def index(request, clienteTemp=None):
    platos = Menu.objects.all()
    data = {
        'platos': platos
    }

    if request.user.is_authenticated:
        clientes = Cliente.objects.all()
        clienteTemp
        for cliente in clientes:
            if cliente.usuario == User.objects.get(username=request.user.username):
                clienteTemp = cliente

        if clienteTemp != None:
            pedidos = Pedido.objects.filter(cliente=Cliente.objects.get(cuil=clienteTemp.cuil))
            data = {
                'platos': platos,
                'clientes': clientes,
                'pedidos': pedidos
            }


    return render(request, 'index/index.html',
                  data)

