from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.urls import reverse, reverse_lazy, is_valid_path

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'station/station.html'
    ordering = '-pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('keyword', '')
        if q:
            queryset = queryset.filter(
                Q(title__iconteains=q) | Q(content__icontains=q)).distinct()
        return queryset


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'station/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self) -> str:
        return reverse


station = PostList.as_view()
create = PostCreate.as_view()
