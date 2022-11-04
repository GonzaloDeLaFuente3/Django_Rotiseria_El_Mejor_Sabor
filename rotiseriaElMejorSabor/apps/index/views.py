from django.shortcuts import render

# Create your views here.
from apps.cliente.models import Cliente
from apps.menu.models import Menu
from apps.administrador.models import Pedido

def index(request):
    platos = Menu.objects.all()
    clientes = Cliente.objects.all()

    data = {
        'platos': platos,
        'clientes': clientes
    }

    if request.user.is_authenticated:
        pedidos = Pedido.objects.filter(cliente=Cliente.objects.get(cuil=12123))
        data = {
            'platos': platos,
            'clientes': clientes,
            'pedidos': pedidos
        }

    return render(request, 'index/index.html',
                  data)

