from django.urls import path

from apps.cliente import views
app_name = 'cliente'
urlpatterns = [

    path('alta', views.altaCliente, name='alta'),
    path('baja', views.bajaCliente, name='baja'),
    path('modificar', views.modificarCliente, name='modificar'),
    path('ver', views.cargarClientes, name='cargar'),

]