
from rest_framework import viewsets
from .serializers.enterprise import EnterpriseSerializer
from .serializers.company import  CompanySerializer
from .serializers.city import CitySerializer
from .models.enterprise import Enterprise
from .models.company import Company
from .models.city import City

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer