from django.urls import path

from apps.administrador import views
apps_name = 'administrador'
urlpatterns = {
    path('', views.administrador, name='administrador'),
}