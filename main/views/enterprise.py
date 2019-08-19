from rest_framework import viewsets
from main.serializers.enterprise import EnterpriseSerializer
from main.models.enterprise import Enterprise


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer