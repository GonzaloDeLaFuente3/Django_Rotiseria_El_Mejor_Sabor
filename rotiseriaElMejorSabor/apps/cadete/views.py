from django.shortcuts import render

# Create your views here.
def cadete_login(request):
    return render(request, 'cadete/cadete-login.html')

def configuracion_cadete(request):
    return render(request, 'cadete/configuracion-cadete.html')