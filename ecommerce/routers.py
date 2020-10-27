from rest_framework import routers
from store.viewsets import ProductViewSet


router = routers.DefaultRouter()
router.register(r'store', ProductViewSet)
