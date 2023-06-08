from django.db import models

# Create your models here.

class Flight(models.Model):
	flightNumber=models.CharField(max_length=10)
	operatingAirLines=models.CharField(max_length=20)
	departureCirty=models.CharField(max_length=20)
	ArrivalCity=models.CharField(max_length=20)
	dateOfDeparture=models.DateField()
	estimatedTimeOfDeparture=models.TimeField()


class Pessanger(models.Model):
	firstName=models.CharField(max_length=10)
	lastName=models.CharField(max_length=20)
	middleName=models.CharField(max_length=20)
	email=models.EmailField()
	phone=models.CharField(max_length=11)
class Reservation(models.Model):
	fligh=models.OneToOneField(Flight,on_delete=models.CASCADE)
	pessanger=models.OneToOneField(Pessanger,on_delete=models.CASCADE)


