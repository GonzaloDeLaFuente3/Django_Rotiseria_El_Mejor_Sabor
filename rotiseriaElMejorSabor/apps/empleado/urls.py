from django.urls import path

from apps.empleado import views
apps_name = 'empleado'
urlpatterns = {

    path('altaEmpleado.html', views.altaEmpleado, name='altaEmpleado'),
    path('bajaCadete.html', views.bajaCadete, name='bajaCadete'),
    path('modificarCadete.html', views.modificarCadete, name='modificarCadete'),
    path('verEmpleados.html', views.verEmpleados, name='verEmpleados'),


}