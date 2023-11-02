from django.urls import path
from . import views

app_name = 'route'

urlpatterns = [
    path('<str:tag_name>/', views.list, name='list'),
    path('<str:tag_name>/create/', views.post_create, name='post_create'),
    path('<str:tag_name>/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:tag_name>/<int:pk>/delete/',
         views.post_delete, name='post_delete'),
]
