from django.contrib import admin
from main.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'category_name']

    def category_name(self, obj):
        return obj.category.name