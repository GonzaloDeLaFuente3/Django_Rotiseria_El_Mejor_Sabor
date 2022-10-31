from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Formulario_registrar
from django.contrib import messages

# Create your views here.
from django.urls import reverse

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
    return render(request, "index/index.html", {"msj":"la sesion de cerro correctamente"})

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
            return redirect(reverse("index:index"))
        data['form']= formulario

    return  render(request, 'navegacion/register.html', data)

