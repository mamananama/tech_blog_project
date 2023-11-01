from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.urls import reverse, reverse_lazy, is_valid_path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Route


class PostList(ListView):
    model = Route
    template_name = 'station/station.html'
    context_object_name = 'routes'
    ordering = '-pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('keyword', '')
        if q:
            queryset = queryset.filter(
                Q(title__iconteains=q) | Q(content__icontains=q)).distinct()
        return queryset


class RouteCreateView(CreateView):
    model = Route


class RouteList(ListView):
    model = Route
    template_name = 'station/station.html'
    context_object_name = 'routes'


class RouteCreate(LoginRequiredMixin, CreateView):
    model = Route

    def form_valid(self, form):
        Route = form.save(commit=False)
        return super().form_valid(form)


list = RouteList.as_view()
# create = PostCreate.as_view()
