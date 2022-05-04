from django.shortcuts import render
from django.views.generic import DetailView

from audi_our_love_shop_project.shop.models import Product


def home(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shop/home-page.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product-page.html'


def checkout(request):
    return render(request, 'shop/checkout-page.html')