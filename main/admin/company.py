from django.contrib import admin
from main.models.company import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display=['name', 'enterprise_name', 'created']

    def enterprise_name(self, obj):
         return obj.enterprise.name