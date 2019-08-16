from django.contrib import admin
from main.models import City

class CityAdmin(admin.ModelAdmin):
    list_display=['name', 'zipcode', 'created']
