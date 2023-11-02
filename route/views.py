from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from station.models import Post
from .models import Route
from station.forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'route/route.html'
    context_object_name = 'posts'
    ordering = '-pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(route__name__icontains=self.kwargs['tag_name']))
        return queryset

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        route_user = Post.objects.filter(
            route__name=self.kwargs['tag_name']).values("author__pk", "author__username").distinct()
        route = Route.objects.get(name=self.kwargs['tag_name'])
        context['route_user'] = route_user
        context['route'] = route
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'route/post.html'
    context_object_name = 'post'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'route/postdelete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('route:route_detail', kwargs={'tag_name': self.kwargs['tag_name']})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'station/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.route = Route.objects.get(name=self.kwargs['tag_name'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('route:route_detail', kwargs={'tag_name': self.kwargs['tag_name']})


list = PostListView.as_view()
post_detail = PostDetailView.as_view()
post_delete = PostDeleteView.as_view()
post_create = PostCreate.as_view()
