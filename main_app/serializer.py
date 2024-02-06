from rest_framework import serializers
from .models import Calls, Clients, Medics, Cars
from .geologic import ClientStreet
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class ClientSerializer(serializers.Serializer):

    clientName = serializers.CharField(max_length=40)
    clientSurname = serializers.CharField(max_length=40)
    phoneNumber = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    sex = serializers.CharField(max_length=1)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
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

        client = Clients.objects.get(id=validated_data['client_id'])
        validated_data['address'] = street
        Calls.objects.create(car_id=None,client_id=client, client_phone=client, 
        diagnose=validated_data['diagnose'], category=validated_data['category'], address=street, lat=validated_data['latitude'], long=validated_data['longitude'])
        return validated_data
    


class CallUpdateSerializer(serializers.Serializer):
  
    is_arrived = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):

        instance.is_arrived = validated_data.get("is_arrived", instance.is_arrived)
        instance.save()
        return instance
        


class CarGeoSerializer(serializers.Serializer):
    lat=serializers.FloatField()
    long=serializers.FloatField()

    def update(self, instance, validated_data):
        instance.lat = validated_data.get("lat", instance.lat)
        instance.long = validated_data.get("long", instance.long)
        instance.save()
        return instance

class CarUpdateSerializer(serializers.Serializer):
    is_working = serializers.BooleanField(required=True)

    def update(self, instance, validated_data):
        instance.is_working = validated_data.get("is_working")
        instance.save()
        return instance
    
class IsArrivedSerializer(serializers.Serializer):
    is_arrived = serializers.BooleanField(required=True)

    def update(self, instance, validated_data):
        instance.is_arrived = validated_data.get("is_arrived")
        instance.save()
        return instance