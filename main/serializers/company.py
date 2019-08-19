from rest_framework import serializers
from main.models.company import Company
from .enterprise import EnterpriseSerializer
from .city import CitySerializer


class  CompanySerializer(serializers.ModelSerializer):
    enterprise =EnterpriseSerializer()
    city =CitySerializer()
    class Meta:
        model = Company
        fields=['id', 'name', 'created', 'enterprise', 'city']
