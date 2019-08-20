
from rest_framework import viewsets
from rest_framework.response import Response
from main.serializers.company import  CompanySerializer
from main.models.company import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field= 'district_id'