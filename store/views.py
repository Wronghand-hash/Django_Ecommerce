from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from .models import *
from rest_framework.decorators import api_view
from django.http import HttpRequest



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

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']



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
        'items':items,
        'order':order
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []


    context = {
        'items':items,
        'order':order
    }
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order , created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem , created = OrderItem.objects.get_or_create(order=order , product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item added to cart', safe=False)