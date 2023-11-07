from django.shortcuts import render


def errorpage404(request, exception):
    return render(request, 'error/error404.html', status=404)


def errorpage500(request, *args, **kwargs):
    return render(request, 'error/error500.html', status=500)
