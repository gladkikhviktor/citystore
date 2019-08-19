from rest_framework import viewsets
from main.serializers.city import CitySerializer
from main.models.city import City

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer