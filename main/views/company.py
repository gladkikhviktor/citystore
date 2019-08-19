
from rest_framework import viewsets
from main.serializers.company import  CompanySerializer
from main.models.company import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer