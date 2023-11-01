from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from station.models import Post, Route
from station.forms import PostForm


class PostView(ListView):
    model = Post
    template_name = 'route/route.html'
    context_object_name = 'posts'
    ordering = '-pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            Q(route__name__icontains=self.kwargs['tag_name']))
        return queryset


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
        print(f'크왉: {self.kwargs}')
        post.route = Route.objects.get(name=self.kwargs['tag_name'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('route:route_detail', kwargs={'tag_name': self.kwargs['tag_name']})


class RouteUserView(ListView):
    model = Post
    template_name = 'route/route_user.html'
    context_object_name = 'route_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            route__name=self.kwargs['tag_name']).values("author__pk", "author__username").distinct()
        print(queryset)
        return queryset


route_detail = PostView.as_view()
post_detail = PostDetailView.as_view()
post_delete = PostDeleteView.as_view()
post_create = PostCreate.as_view()
route_user = RouteUserView.as_view()
