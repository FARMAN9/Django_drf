from rest_framework import serializers
from .models import *



class CarSer(serializers.ModelSerializer):
    

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'color', 'price', 'is_available']
        
        
    