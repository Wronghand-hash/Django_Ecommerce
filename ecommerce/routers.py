from rest_framework import routers
from store.viewsets import ProductViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'store', ProductViewSet)
router.register(r'category', CategoryViewSet)
