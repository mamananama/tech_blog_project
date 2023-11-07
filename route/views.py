from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Route
from .forms import PostForm, RouteForm, RouteEditForm


class PostListView(ListView):
    model = Post
    template_name = 'route/route.html'
    context_object_name = 'posts'
    ordering = '-updated_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(route__name__iexact=self.kwargs['tag_name']))
        q = self.request.GET.get('keyword', '')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)).distinct()
        return queryset

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        route_user = Post.objects.filter(
            route__name__iexact=self.kwargs['tag_name']).values("author__pk", "author__username").distinct()
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
        post.save(update_fields=('count',))
        return super().get_object(queryset)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        route_user = Post.objects.filter(
            route__name__iexact=self.kwargs['tag_name']).values("author__pk", "author__username").distinct()
        route = Route.objects.get(name=self.kwargs['tag_name'])
        posts = Post.objects.filter(
            Q(route__name__iexact=self.kwargs['tag_name']))

        context['route_user'] = route_user
        context['route'] = route
        context['posts'] = posts
        return context


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

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'CREATE POST @ROUTE: {self.kwargs['tag_name']}'
        context['page_title'] = page_title
        return context


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'route/postdelete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('route:list', kwargs={'tag_name': self.kwargs['tag_name']})

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'DELETE POST @ROUTE: {
            self.kwargs['tag_name']}'
        context['page_title'] = page_title
        return context


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
        return reverse('route:post_detail', kwargs={'tag_name': self.kwargs['tag_name'], 'pk': self.kwargs['pk']})

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'EDIT POST @ROUTE: {
            self.kwargs['tag_name']}'
        context['page_title'] = page_title
        return context


class RouteUpdate(UserPassesTestMixin, UpdateView):
    model = Route
    form_class = RouteEditForm
    template_name = 'station/create.html'

    def get_object(self):
        object = get_object_or_404(Route, name=self.kwargs['tag_name'])
        return object

    def form_valid(self, form):
        route = form.save(commit=False)
        route.cheif = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('route:list', kwargs={'tag_name': self.kwargs['tag_name']})

    def test_func(self):
        return self.get_object().cheif == self.request.user

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_title = f'EDIT STATUS of ROUTE: {
            self.kwargs['tag_name']}'
        context['page_title'] = page_title
        return context


list = PostListView.as_view()
post_detail = PostDetailView.as_view()
post_create = PostCreate.as_view()
post_edit = PostUpdate.as_view()
post_delete = PostDeleteView.as_view()
route_edit = RouteUpdate.as_view()
