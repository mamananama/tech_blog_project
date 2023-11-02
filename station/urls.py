from django.urls import path, include
from . import views

app_name = 'station'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.route_create, name='route_create'),
]
