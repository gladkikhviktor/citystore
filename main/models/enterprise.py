from django.db import models
from .common import Common


class Enterprise(Common):
    name = models.TextField(max_length=250, blank=False,  default='')

    def __str__(self):
        return self.name
        
    class Meta:
        db_table='enterprise'