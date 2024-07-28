from django.contrib import admin
from .models import Person
from .models import Product
from .models import OrderDetail

# Register your models here.

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(OrderDetail)
