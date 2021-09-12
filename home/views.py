from django.shortcuts import render


def index(request):
    """ A view to render index.html """

    return render(request, "home/index.html")
