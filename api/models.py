from django.db import models

# Create your models here.

class Person(models.Model):
    fullname = models.CharField(max_length=250)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)