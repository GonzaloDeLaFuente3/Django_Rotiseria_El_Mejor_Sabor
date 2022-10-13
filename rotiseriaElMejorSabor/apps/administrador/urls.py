from django.urls import path

from apps.administrador import views
apps_name = 'administrador'
urlpatterns = {
    #path('', views.administrador, name='administrador'),
    #/admin/configuracion-admin.html
    path('admin-login.html', views.admin_login, name='admin_login'),
    path('configuracion-admin.html', views.administrador_configuracion, name='administrador_configuracion'),
    path('pedido.html', views.pedido, name='pedido'),
    path('estadisticas.html', views.estadisticas, name='estadisticas'),
    path('historial-pedidos.html', views.historial_pedidos, name='historial_pedidos'),
}