from rest_framework import serializers
from main.models import Product
from .category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model= Product
        fields=['id', 'name', 'category', 'created']
    