from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView

from audi_our_love_shop_project.shop.models import Product, OrderProduct, Order


def home(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shop/home-page.html', context)


@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product_id=product.pk).exists():
            order_product.quantity += 1
            order_product.save()
            return redirect(reverse('product', kwargs={'pk': product.pk}))
        else:
            order.items.add(order_product)
            messages.info(request, "This item was added to your cart.")
            return redirect(reverse('product', kwargs={'pk': product.pk}))
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_product)
        messages.info(request, "This item was added to your cart.")
        return redirect(reverse('product', kwargs={'pk': product.pk}))


@login_required
def remove_from_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product_id=product.id).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_product)
            order_product.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect(reverse('product', kwargs={'pk': product.pk}))
        else:
            messages.info(request, "This item was not in your cart")
            return redirect(reverse('product', kwargs={'pk': product.pk}))
    else:
        messages.info(request, "You do not have an active order")
        return redirect(reverse('product', kwargs={'pk': product.pk}))


@login_required
def remove_single_item_from_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product_id=product.pk).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.items.remove(order_product)
            messages.info(request, "This item quantity was updated.")
            return redirect(reverse('product', kwargs={'pk': product.pk}))
        else:
            messages.info(request, "This item was not in your cart")
            return redirect(reverse('product', kwargs={'pk': product.pk}))
    else:
        messages.info(request, "You do not have an active order")
        return redirect(reverse('product', kwargs={'pk': product.pk}))


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product-page.html'


def checkout(request):
    return render(request, 'shop/checkout-page.html')
