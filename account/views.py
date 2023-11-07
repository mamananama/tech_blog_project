from typing import Any
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

from route.models import Post


class SignupCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:welcome')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'SIGN UP'
        context['page_title'] = page_title
        return context


class TrainLoginView(LoginView):
    template_name = 'account/login.html'
    next_page = 'main:index'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'LOGIN'
        context['page_title'] = page_title
        return context


class TrainLogoutView(LogoutView):
    next_page = 'main:index'


class ProfileDetailView(DetailView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        queryset = super().get_queryset()
        queryset = queryset.get(username__exact=self.kwargs['user_name'])
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        routes = Post.objects.filter(
            author__username__exact=self.kwargs['user_name']).values('route__name').distinct()
        recents = Post.objects.filter(
            author__username__exact=self.kwargs['user_name']).order_by('-created_at')[:10]

        context['routes'] = routes
        context['recents'] = recents
        return context


signup = SignupCreateView.as_view()
login = TrainLoginView.as_view()
logout = TrainLogoutView.as_view()
profile = ProfileDetailView.as_view()


def welcome(request):
    return render(request, 'account/welcome.html')
