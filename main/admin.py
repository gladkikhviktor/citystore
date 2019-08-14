from django.contrib import admin, sites
from .models import City, District, Category


# Register your models here.
admin.site.register(City)
admin.site.register(District)
admin.site.register(Category)