from django.shortcuts import render


def home(request):
    return render(request, 'shop/home-page.html')


def product(request):
    return render(request, 'shop/product-page.html')


def checkout(request):
    return render(request, 'shop/checkout-page.html')