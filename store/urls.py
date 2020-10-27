from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('cart/', views.cart, name="cart"),
    path('store/', views.store , name="store"),
    path('checkout/', views.checkout, name="checkout"),
    path('<slug:category_slug>/<slug:slug>', views.product_detail, name="product_detail"),
    path('<slug:slug>', views.category_detail, name="category_detail"),
]