from django.shortcuts import render

from api.models import Flight,Pessanger,Reservation

from api.serializers import FlightSerializer,PessangerSerializer,ReservationSerializer

from rest_framework import viewsets

from rest_framework.decorators import api_view,permission_classes

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
# Create your views here.

# we will be using viewsets

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def findFlights(reqeust):

	flights=Flight.objects.filter(departureCirty=reqeust.data['departureCirty'],ArrivalCity=reqeust.data['ArrivalCity'],dateOfDeparture=reqeust.data['dateOfDeparture'])
	serializer=FlightSerializer(flights,many=True)
	return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
	queryset=Flight.objects.all()
	serializer_class=FlightSerializer

class PessangerViewSet(viewsets.ModelViewSet):
	queryset=Reservation.objects.all()
	serializer_class=PessangerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
	queryset=Reservation.objects.all()
	serializer_class=ReservationSerializer


