from rest_framework import serializers
from main.models import Price

from .company import CompanySerializer
from .product import ProductSerializer
from .category import CategorySerializer


class PriceSerializer(serializers.ModelSerializer):
        company = CompanySerializer()
        product = ProductSerializer()
        class Meta:
            model = Price
            fields=['id', 'price', 'date_begin', 'date_end', 'product', 'company', 'created']
