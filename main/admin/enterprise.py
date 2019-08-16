from django.contrib import admin
from main.models import Enterprise

class EnterpriseAdmin(admin.ModelAdmin):
    list_display=['name']