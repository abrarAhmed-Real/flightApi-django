from rest_framework import serializers

from api.models import Flight,Pessanger,Reservation

class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model=Flight
		fields='__all__'

class PessangerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Pessanger
		fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Reservation
		fields='__all__'
