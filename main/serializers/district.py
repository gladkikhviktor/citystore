from rest_framework import serializers
from main.models.district import District
from .city import CitySerializer


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model=District
        fields=['id', 'name', 'city', 'created']
        
