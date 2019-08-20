from rest_framework import viewsets
from main.serializers.district import DistrictSerializer
from main.models.district import District

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer