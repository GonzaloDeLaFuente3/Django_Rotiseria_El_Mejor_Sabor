from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import lower

from .forms import Formulario_registrar
from django.contrib import messages

# Create your views here.
from django.urls import reverse

from apps.menu.models import Menu
from apps.administrador.models import Pedido

from ..administrador.forms import PedidoForm
from ..cliente.models import Cliente


def ayuda(request):
    return  render(request, 'navegacion/ayuda.html')

def contacto(request):
    return  render(request, 'navegacion/contacto.html')

def sobreNosotros(request):
    return  render(request, 'navegacion/sobreNosotros.html')

def comprar(request, id, clienteTemp=None):
    if request.user.is_authenticated:
        clientes = Cliente.objects.all()
        usuario = User.objects.get(username=request.user.username)
        plato = Menu.objects.get(id=id)
        clienteTemp

        for cliente in clientes:
            if cliente.usuario == usuario:
                clienteTemp = cliente

        if clienteTemp != None:
            return render(request, 'navegacion/comprar.html', {'plato': plato, 'cliente': cliente})
        else:
            return redirect(reverse("cliente:registrar_cliente"))
    else:
        return redirect(reverse("navegacion:login"))


def altaPedidoCliente(request):
    fechaPedido = request.POST['fechaPedido']
    fecha_hora = request.POST['fecha_hora']
    cliente = request.POST['cliente']
    tiempoDemora = request.POST['tiempoDemora']
    cadete = request.POST['cadete']
    total = request.POST['total']

    menu = request.POST['menu']
    estadoPedido = request.POST['estadoPedido']
    comentario = lower(request.POST['comentario'])
    envioDomicilio = request.POST['envioDomicilio']

    pedido = Pedido.objects.create(fechaPedido=fechaPedido, estadoPedido= estadoPedido, comentario = comentario, envioDomicilio=envioDomicilio,
    tiempoDemora=tiempoDemora, total=total, cadete_id=cadete,cliente_id=cliente,fecha_hora=fecha_hora)
    messages.success(request, "se registro el pedido correctamente")
    return redirect(reverse("index:index"))

def configuracion(request):
    return  render(request, 'navegacion/configuracion.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST["usuario"]
        password = request.POST["contraseña"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index:index"))
        else:
            return  render(request, 'navegacion/login.html', {"msj":"Los datos ingresados son incorrectos"})
    return  render(request, 'navegacion/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Se cerro la sesion correctamente")
    return redirect(reverse("index:index"))
    # return render(request, "navegacion/login.html", {"msj":"la sesion de cerro correctamente"})

def recuperarContraseña(request):
    return  render(request, 'navegacion/recuperarContraseña.html')
def register(request):
    data ={
        'form': Formulario_registrar()
    }
    if request.method == 'POST':
        formulario = Formulario_registrar(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticacion
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Usted se registro correctamente")
            return redirect(reverse("cliente:registrar_cliente"))
        data['form']= formulario

    return  render(request, 'navegacion/register.html', data)

