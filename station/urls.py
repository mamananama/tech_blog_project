from django.urls import path, include
from . import views

app_name = 'station'

urlpatterns = [
    path('', views.station, name='station'),
    path('create/', views.create, name='create'),
    # path('station/route/', include('route.urls')),
]
