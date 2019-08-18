from rest_framework import serializers
from main.models.city import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields=['name', 'created']