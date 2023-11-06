from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q
from django.urls import reverse, reverse_lazy, is_valid_path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from route.models import Route, Post
from route.forms import RouteForm


class RouteList(ListView):
    model = Route
    template_name = 'station/station.html'
    context_object_name = 'routes'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        post_number = {}
        for route in context['routes']:
            print(str(route))
            post_number[str(route)] = Post.objects.filter(
                route__name__exact=route).distinct().count()
        print(post_number)
        context['post_number'] = post_number
        return context


class RouteCreate(LoginRequiredMixin, CreateView):
    model = Route
    form_class = RouteForm
    template_name = 'station/create.html'

    def form_valid(self, form):
        route = form.save(commit=False)
        route.cheif = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('station:list')


list = RouteList.as_view()
create = RouteCreate.as_view()
