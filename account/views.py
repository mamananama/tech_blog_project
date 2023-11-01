from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse

from station.models import Post

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name='account/signup.html',
    success_url=reverse_lazy('account:login'),
)

login = LoginView.as_view(
    template_name='account/login.html',
    next_page='main:index',
)

logout = LogoutView.as_view(
    next_page='main:index',
)

# profile = DetailView(
#     model =
# )
