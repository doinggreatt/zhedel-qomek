from rest_framework import serializers
from .models import Calls, Cars
from .geologic import ClientStreet
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class CallSerializer(serializers.Serializer):

    client_name = serializers.CharField()
    client_number = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    diagnose= serializers.CharField(max_length=20)
    category = serializers.IntegerField()
    address = serializers.CharField(required=False)

    def create(self, validated_data):
        street = ClientStreet(validated_data['latitude'], validated_data['longitude']).output

        validated_data['address'] = street
        Calls.objects.create(car_id=None,client_name=validated_data['client_name'], client_phone=validated_data['client_number'], 
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