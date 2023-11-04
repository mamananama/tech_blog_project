from django.shortcuts import render
from django.views.generic import ListView

from route.models import Post, Route


def index(request):
    return render(request, 'main/index.html')


class MainListView(ListView):
    model = Route
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        routes = Route.objects.all()
        print(routes)
        context['routes'] = routes
        return context


index = MainListView.as_view()
