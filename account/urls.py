from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:user_name>/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
]

handler404 = 'train.views.errorpage404'
