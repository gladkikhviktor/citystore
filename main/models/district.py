from django.db import models
from .common import Common
from .city import City

#район города
class District(Common):
     city = models.ForeignKey(City, on_delete=models.CASCADE)
     name = models.TextField(max_length=250, blank=False,  default='')

     def __str__(self):
      return self.name

     class Meta:
        db_table = 'district'