from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PersonSerializer, ProductSerializer, OrderDetailSerializer
from .models import Person, Product, OrderDetail
# Create your views here.

class PersonViewSets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderDetailViewSets(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer