from rest_framework import routers
from django.urls import path, include
from .views import StockViewSet, WatchlistViewSet

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'watchlists', WatchlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
