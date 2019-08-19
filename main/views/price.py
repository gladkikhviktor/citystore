from rest_framework import viewsets
from main.serializers.price import PriceSerializer
from main.models.price import Price


class PriceViewSet(viewsets.ModelViewSet):
    queryset= Price.objects.all()
    serializer_class = PriceSerializer
