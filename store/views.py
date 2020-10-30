from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.decorators import api_view
from django.http import HttpRequest
from rest_framework import viewsets
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




def frontpage(request):
    products = Product.objects.all()

    context = {
        'products':products
    }

    return render(request, 'store/frontpage.html', context)


def product_detail(request,category_slug, slug):
    product = get_object_or_404(Product,slug=slug)
    
    context = {
        'product': product
    }

    return render(request, 'store/product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.Products.all()

    context = {
        'category':category,
        'products':products
    }

    return render(request, 'store/category_detail.html', context)
def store(request):
    products = Product.objects.all()

    context = {
        'products':products
    }
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []


    context = {
        'items':items
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
