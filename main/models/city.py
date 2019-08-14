from django.db import models
from .common import Common

#Города
class City(Common):
    name = models.TextField(max_length=250, unique=True,blank=False,  default='')
    zipcode = models.CharField(max_length=6, unique=True, blank=False, default='000000') 