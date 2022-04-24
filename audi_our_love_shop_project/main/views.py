from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about/about.html')
