from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from main.serializers.product import ProductSerializer
from main.models.product import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']