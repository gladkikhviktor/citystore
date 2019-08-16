from django.contrib import admin
from main.models import Price

class PriceAdmin(admin.ModelAdmin):
    list_display=['product_name', 'enterprise_name','price', 'date_begin', 'date_end']

    def product_name(self, obj):
        return obj.product.name

    def enterprise_name(self, obj):
        return obj.enterprise.name