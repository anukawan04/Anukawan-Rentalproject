from rest_framework import serializers
from .models import Vehicles


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['user', 'vehicle_number', 'vehicle_model', 'vehicle_type','color']