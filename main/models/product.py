from django.db import models
from .common import Common
from .category import Category

# Товар
class Product(Common):
     name = models.TextField(max_length=250, blank=False,  default='')
     category = models.ForeignKey(Category, on_delete=models.CASCADE)