from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('', views.frontpage, name="frontpage"),
    # path('cart/', views.cart, name="cart"),
    # path('store/', views.store , name="store"),
    # path('checkout/', views.checkout, name="checkout"),
    # path('<slug:category_slug>/<slug:slug>', views.product_detail, name="product_detail"),
    # path('<slug:slug>', views.category_detail, name="category_detail"),

    path('store/', views.ProductList.as_view(), name="ProductViewSet"),
    path('store/<int:pk>/', views.ProductList.as_view(), name="product_detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]