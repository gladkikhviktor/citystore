from rest_framework import serializers
from main.models.company import Company
from .enterprise import EnterpriseSerializer
from .city import CitySerializer
from .district import DistrictSerializer

class  CompanySerializer(serializers.HyperlinkedModelSerializer):
    enterprise = EnterpriseSerializer()
    city = CitySerializer()
    district = DistrictSerializer()
    class Meta:
        model = Company
        fields=['id', 'name', 'created', 'enterprise', 'city', 'district']
        lookup_field= 'district_id'
        extra_kwargs = {
                'url': {'lookup_field': 'district_id'}
            }