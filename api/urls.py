from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSets)
router.register(r'products', views.ProductViewSets)
router.register(r'orderDetails', views.OrderDetailViewSets)

urlpatterns = [
    path('', include(router.urls))
]