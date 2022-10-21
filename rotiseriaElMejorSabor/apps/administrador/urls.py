from django.urls import path

from apps.administrador import views
app_name = 'administrador'
urlpatterns = [
    #path('', views.administrador, name='administrador'),
    #/admin/configuracion-admin.html
    path('admin-login/', views.admin_login, name='admin_login'),
    path('configuracion-admin/', views.administrador_configuracion, name='administrador_configuracion'),
    path('pedido/', views.pedido, name='pedido'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('historial-pedidos/', views.historial_pedidos, name='historial_pedidos'),
]