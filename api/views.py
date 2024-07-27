from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PersonSerializer
from .models import Person
# Create your views here.

class PersonViewSets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer