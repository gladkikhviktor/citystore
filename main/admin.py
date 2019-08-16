from django.contrib import admin, sites
from .models import City, District, Category, Enterprise, Product, Price


# Register your models here.
admin.site.register(City)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Enterprise)
admin.site.register(Product)
admin.site.register(Price)