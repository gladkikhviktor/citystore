from rest_framework import viewsets
from main.serializers.category import CategorySerializer
from main.models.category import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer