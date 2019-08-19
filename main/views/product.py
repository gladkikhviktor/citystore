from rest_framework import viewsets
from main.serializers.product import ProductSerializer
from main.models.product import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer