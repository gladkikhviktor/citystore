from django.contrib import admin
from main.models import Price

class PriceAdmin(admin.ModelAdmin):
    list_display=['product_name', 'enterprise_name', 'city_name', 'company_name', 'price', 'date_begin', 'date_end', 'created']

    def product_name(self, obj):
        return obj.product.name

    def company_name(self, obj):
        return obj.company.name

    def enterprise_name(self, obj):
        return obj.company.enterprise.name

    def city_name(self, obj):
        return obj.company.city.name