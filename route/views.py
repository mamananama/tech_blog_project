from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.count += 1
        post.save()
        return super().get_object(queryset)


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
        return reverse('route:post_detail', kwargs={'tag_name': self.kwargs['tag_name'], 'pk': self.object.id})


class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'station/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.route = Route.objects.get(name=self.kwargs['tag_name'])
        return super().form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('route:post_detail', kwargs={'tag_name': self.kwargs['tag_name'], 'pk': self.kwargs['pk']})

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'route/postdelete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('route:list', kwargs={'tag_name': self.kwargs['tag_name']})

    def test_func(self):
        return self.get_object().author == self.request.user


list = PostListView.as_view()
post_detail = PostDetailView.as_view()
post_create = PostCreate.as_view()
post_edit = PostUpdate.as_view()
post_delete = PostDeleteView.as_view()
