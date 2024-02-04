from rest_framework import serializers
from .models import Calls, Clients, Medics

class ClientSerializer(serializers.Serializer):
    clientName = serializers.CharField(max_length=40),
    clientSurname  = serializers.CharField(max_length=40)
    phoneNumber = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    sex = serializers.CharField(max_length=1)
