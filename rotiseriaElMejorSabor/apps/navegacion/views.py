from django.shortcuts import render

# Create your views here.
from apps.menu.models import Menu
from apps.administrador.models import Pedido

def ayuda(request):
    return  render(request, 'navegacion/ayuda.html')

def contacto(request):
    return  render(request, 'navegacion/contacto.html')

def sobreNosotros(request):
    return  render(request, 'navegacion/sobreNosotros.html')

def comprar(request, id):
    plato = Menu.objects.get(id=id)
    return  render(request,
                   'navegacion/comprar.html',
                   {'plato':plato})

def comprar_form_submission(request):

    fechaPedido = request.POST['fechaPedido']
    horaPedido = request.POST['horaPedido']
    nombreMenu = lower(request.POST['nombreMenu'])
    precioMenu = request.POST['precioMenu']
    cliente = request.POST['cliente']
    domicilio = request.POST['domicilio']
    tipoEntrega = request.POST['tipoEntrega']
    estado = request.POST['estadoPedido']

    pedido = Pedido.objects.create(fechaPedido=fechaPedido, menu=nombreMenu, total=precioMenu, clienteo=cliente,
                               vigencia=vigencia, tipoComida=tipo_comida, imagen=imagen)
    messages.success(request, "se registro el menu correctamente")
    return redirect(reverse('index/index.html',
                  {'platos':platos}))

def configuracion(request):
    return  render(request, 'navegacion/configuracion.html')

def login(request):
    return  render(request, 'navegacion/login.html')

def recuperarContraseña(request):
    return  render(request, 'navegacion/recuperarContraseña.html')
def register(request):
    return  render(request, 'navegacion/register.html')

