from rest_framework import serializers
from .models import Calls, Clients, Medics, Cars
from .geologic import ClientStreet
from rest_framework.response import Response


class ClientSerializer(serializers.Serializer):
 #   class Meta:
 #       model = Clients 
 #       fields = "__all__"
   
   
    clientName = serializers.CharField(max_length=40)
    clientSurname = serializers.CharField(max_length=40)
    phoneNumber = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    sex = serializers.CharField(max_length=1)

    def create(self, validated_data):
        return Clients.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.clientName = validated_data.get("clientName", instance.clientName)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance





class CallSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    diagnose= serializers.CharField(max_length=20)
    category = serializers.IntegerField()
    address = serializers.CharField(required=False)

    def create(self, validated_data):
        street = ClientStreet(validated_data['latitude'], validated_data['longitude']).output
        car_id = Cars.objects.get(id=1) 
        client = Clients.objects.get(id=1)
        validated_data['address'] = street
        Calls.objects.create(car_id=car_id, client_id=client, client_phone=client, 
        diagnose=validated_data['diagnose'], category=validated_data['category'], address=street)
        return validated_data
        
    