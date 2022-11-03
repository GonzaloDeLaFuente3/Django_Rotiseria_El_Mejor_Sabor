from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
@permission_required('empleado.add_empleado', login_url="navegacion:login")
def cadete_login(request):
    return render(request, 'cadete/cadete-login.html')

@permission_required('empleado.change_empleado', login_url="navegacion:login")
def configuracion_cadete(request):
    return render(request, 'cadete/configuracion-cadete.html')