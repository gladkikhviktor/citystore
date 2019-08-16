from django.db import models
from .common import Common
from .category import Category

# Товар
class Product(Common):
     name = models.TextField(max_length=250, blank=False,  default='')
     category = models.ForeignKey(Category, on_delete=models.CASCADE)

     def __str__(self):
          return self.name

     class Meta:
          db_table='product'