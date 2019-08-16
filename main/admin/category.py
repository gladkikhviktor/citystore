from django.contrib import admin
from main.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
