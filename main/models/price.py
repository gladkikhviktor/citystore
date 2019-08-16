from django.db import models
from .common import Common
from .product import Product
from .enterprise import Enterprise

class Price(Common):
    price = models.DecimalField(max_digits=15, decimal_places=2)
    date_begin = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)