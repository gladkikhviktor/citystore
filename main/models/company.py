from django.db import models
from .common import Common
from .city import City
from .enterprise import Enterprise
from .district import District


class Company(Common):
    name = models.TextField(max_length=250, blank=False,  default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table='company'