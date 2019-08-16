from django.contrib import admin
from main.models import District

class DistrictAdmin(admin.ModelAdmin):
    list_display=['name', 'city_name', 'created']

    def city_name(self, obj):
        return obj.city.name