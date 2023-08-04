from rest_framework import serializers

from .models import Area,Region,Measurements

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        #esto es de maneta selectiva
        """fields = ['id',
                  'name',
                  'owner',
                  'phone',
                  'mail',
                  'country',
                  'state',
                  'city',
                  'postal_code',
                  'creat_at',
                 ]"""
        #esto es de manera automatica
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'area',
            'name',
            'latitude',
            'longitude',
            'created_at',
        ]

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields= '__all__'