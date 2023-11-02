from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.urls import reverse, reverse_lazy, is_valid_path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from route.models import Route
from route.forms import RouteForm


class RouteList(ListView):
    model = Route
    template_name = 'station/station.html'
    context_object_name = 'routes'


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
route_create = RouteCreate.as_view()
