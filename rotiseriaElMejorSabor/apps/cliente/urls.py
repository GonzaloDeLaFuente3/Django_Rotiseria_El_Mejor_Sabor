from django.urls import path

from apps.cliente import views
apps_name = 'cliente'
urlpatterns = {

    path('altaCliente.html', views.altaCliente, name='altaCliente'),
    path('bajaCliente.html', views.bajaCliente, name='bajaCliente'),
    path('modificarCliente.html', views.modificarCliente, name='modificarCliente'),
    path('verClientes.html', views.verClientes, name='verClientes'),

}