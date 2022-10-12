from django.urls import path

from apps.index import views
apps_name = 'index'
urlpatterns = {
    path('', views.index, name='index'),
}