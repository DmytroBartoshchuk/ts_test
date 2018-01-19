from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        # fields = '__all__'
        fields = ('carrier', 'departure_city', 'arrive_city', 'date')
