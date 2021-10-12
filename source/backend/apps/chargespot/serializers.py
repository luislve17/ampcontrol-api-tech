from rest_framework import serializers
from .models import Chargespot

class ChargespotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chargespot
        fields = ('name', 'lat', 'lng', 'last_maintenance_date')