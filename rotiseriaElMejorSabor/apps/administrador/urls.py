from django.urls import path
from django.views.generic import TemplateView

from apps.administrador import views
app_name = 'administrador'
urlpatterns = [
    #path('', views.administrador, name='administrador'),
    #/admin/configuracion-admin.html
    # TemplateView.as_view(template_name='base/home.html')
    path('admin-login/', views.admin_login, name='admin_login'),
    path('configuracion-admin/', views.administrador_configuracion, name='administrador_configuracion'),
    path('pedido/', views.registrar_pedido, name='pedido'),
    path('estadisticas/', views.estadistica_principal, name='estadisticas'),
    path('historial-pedidos/', views.historial_pedidos, name='historial_pedidos'),
    path('modificar_pedido/<int:id>', views.modificar_pedido, name='modificar'),
    # path('editar_pedido/', views.editar_pedido, name='editar_pedido'),
    path('consulta_cadete/', views.estadisticas, name='consulta_cadete'),
    path('consulta_fecha/', views.consulta_fecha, name='consulta_fecha'),
    path('estado_pedido_delivery/', views.estado_pedido, name='estado_pedido'),
    path('editar_estado_pedido_delivery/<int:id>', views.editar_estado_pedido, name='editar_estado_pedido'),

]