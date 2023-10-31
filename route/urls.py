from django.urls import path
from . import views

app_name = 'route'

urlpatterns = [
    path('<str:tag_name>/', views.route, name='route'),
    #     path('<str:tag_name>/create/', views.route, name='r_create'),
    path('<str:tag_name>/<int:pk>/', views.post_detail, name='post_detail'),
    #     path('<str:tag_name>/<int:pk>/delete/',
    #          views.post_delete, name='post_delete'),
    #     path('<str:tag_name>/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #     path('<str:tag_name>/<int:pk>/comment/',
    #          views.post_comment, name='post_comment'),
]
