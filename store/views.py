from django.shortcuts import render
from django.http import HttpResponse, JsonResponse , Http404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer


from rest_framework import mixins
from rest_framework import generics


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


#class based api using 
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self , request , *args , **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset , many=True)
        return Response(serializer.data)


    def post(self, request, *args , **kwargs):
        return self.create(request, *args , **kwargs)
      
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# def frontpage(request):
#     products = Product.objects.all()

#     context = {
#         'products':products
#     }

#     return render(request, 'store/frontpage.html', context)


# def product_detail(request,category_slug, slug):
#     product = get_object_or_404(Product,slug=slug)
    
#     context = {
#         'product': product
#     }

#     return render(request, 'store/product_detail.html', context)


# def category_detail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products = category.Products.all()

#     context = {
#         'category':category,
#         'products':products
#     }

#     return render(request, 'store/category_detail.html', context)
# def store(request):
#     products = Product.objects.all()

#     context = {
#         'products':products
#     }
#     return render(request, 'store/store.html', context)

# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order , created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []


#     context = {
#         'items':items
#     }
#     return render(request, 'store/cart.html', context)

# def checkout(request):
#     context = {}
#     return render(request, 'store/checkout.html', context)
