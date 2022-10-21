from django.urls import path

from apps.empleado import views
app_name = 'empleado'
urlpatterns = [

    path('alta', views.altaEmpleado, name='alta'),
    path('modificar_cadete', views.modificarCadete, name='modificar_cadete'),
    path('ver', views.verEmpleados, name='ver'),


]