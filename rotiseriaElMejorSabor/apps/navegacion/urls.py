from django.urls import path

from apps.navegacion import views
apps_name = 'navegacion'
urlpatterns = [
    path('ayuda.html', views.ayuda, name='ayuda'),
    path('contacto.html', views.contacto, name='contacto'),
    path('sobreNosotros.html', views.sobreNosotros, name='sobreNosotros'),
    path('comprar.html', views.comprar, name='comprar'),
    path('configuracion.html', views.configuracion, name='configuracion'),
    path('login.html', views.login, name='login'),
    path('recuperarContraseña.html', views.recuperarContraseña, name='recuperarContraseña'),
    path('register.html', views.register, name='register'),

]