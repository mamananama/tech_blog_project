from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from route.models import Post, Route


def index(request):
    return render(request, 'main/index.html')


class MainListView(ListView):
    model = Route
    template_name = "main/index.html"
    context_object_name = 'routes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        routes = Route.objects.all()
        hit_posts = Post.objects.order_by('-count')[:10]
        recent_posts = Post.objects.order_by('-created_at')[:10]

        post_number = {}
        route_status = {}
        for route in context['routes']:
            post_number[str(route)] = Post.objects.filter(
                route__name__exact=str(route)).distinct().count()
            route_status[str(route)] = route.status

        print(post_number)
        print(route_status)

        context['routes'] = routes
        context['hit_posts'] = hit_posts
        context['recent_posts'] = recent_posts
        context['post_number'] = post_number
        context['route_status'] = route_status
        return context


index = MainListView.as_view()
