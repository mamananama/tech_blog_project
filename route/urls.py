from django.urls import path
from . import views

app_name = 'route'

urlpatterns = [
    path('<str:tag_name>/', views.list, name='list'),
    path('<str:tag_name>/route_edit/', views.route_edit, name='route_edit'),
    path('<str:tag_name>/create/', views.post_create, name='post_create'),
    path('<str:tag_name>/<int:pk>/', views.post_detail, name='post_detail'),
    path('<str:tag_name>/<int:pk>/post_delete/',
         views.post_delete, name='post_delete'),
    path('<str:tag_name>/<int:pk>/post_edit/',
         views.post_edit, name='post_edit'),
    path('<str:tag_name>/<int:pk>/comment/',
         views.post_comment, name='post_comment'),
    path('<str:tag_name>/<int:post_pk>/comment_delete/<int:pk>/',
         views.post_comment_delete, name='post_comment_delete'),
]
