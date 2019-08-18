from rest_framework import serializers
from main.models.enterprise import Enterprise

class  EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields=['name',  'created']

