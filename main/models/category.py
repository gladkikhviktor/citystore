from django.db import models
from .common import Common

class Category(Common):
    name = models.TextField(max_length=250, unique=True,blank=False,  default='')