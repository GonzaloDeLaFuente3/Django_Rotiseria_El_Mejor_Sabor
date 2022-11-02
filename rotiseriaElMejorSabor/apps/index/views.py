from django.shortcuts import render

# Create your views here.
from apps.cliente.models import Cliente
from apps.menu.models import Menu
def index(request):
    platos = Menu.objects.all()
    clientes = Cliente.objects.all()

    data = {
        'platos': platos,
        'clientes': clientes
    }

    return render(request, 'index/index.html',
                  data)

