from django.urls import path

from apps.navegacion import views
app_name = 'navegacion'
urlpatterns = [
    path('ayuda', views.ayuda, name='ayuda'),
    path('contacto', views.contacto, name='contacto'),
    path('sobre_nosotros', views.sobreNosotros, name='sobre_nosotros'),
    path('comprar/<int:id>', views.comprar, name='comprar'),
    path('configuracion', views.configuracion, name='configuracion'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('recuperar_contraseña.html', views.recuperarContraseña, name='recuperar_contraseña'),
    path('register', views.register, name='register'),

]