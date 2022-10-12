from rest_framework import serializers
from .models import *




class ContinentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continents
        fields = '__all__'