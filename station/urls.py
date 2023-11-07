from django.urls import path, include
from . import views

app_name = 'station'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
]

handler404 = 'train.views.errorpage404'
