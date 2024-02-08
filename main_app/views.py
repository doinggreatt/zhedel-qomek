from django.shortcuts import render
from rest_framework import generics, status
from .models import Calls, Cars, CarsPosition
from .serializer import  CallSerializer, CallUpdateSerializer, CarUpdateSerializer, CarGeoSerializer, IsArrivedSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import redis, json
from zhedel_qomek import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.forms import model_to_dict
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)
from .geologic import FindNearest



class CallCreate(APIView):
    def post(self, request): # Creating new call with POST request
        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data

        return Response({"data": {"status": "call created", "address":serializer.data['address']}}, status=status.HTTP_200_OK) 

    def put(self, request, *agrs, **kwargs): # UPDATE request for updating call's status / created or not
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Calls.objects.get(pk=pk)
        except:
            return Response({"error":"Object does not exists"})

        serializer = CallUpdateSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data_put": serializer.data})

    def get(self, request, *args, **kwargs):

        id = kwargs.get("id", None)
        instance = Calls.objects.get(id=id)
        if instance.is_accepted == False:
            _car = FindNearest(instance.lat, instance.long)
            nearest_car = _car.find_nearest()
            if nearest_car: # Если ближайшая машина нашлась, нужно зарегистрировать адрес вызова для водителя!
                distance = nearest_car['distance']
                instance.is_accepted=True
                instance.car_id_id  =Cars.objects.get(id=nearest_car['id'])
                current_car = CarsPosition.objects.get(car_id = instance.car_id_id)
                car_lat = current_car.lat 
                car_long = current_car.long
                current_car.call_address = instance.address
                print(current_car.call_address)
                current_car.save()
                print(current_car.call_address)
                instance.save()
                return Response({"lat": car_lat, "long": car_long})
            else: # Если ближайшая машина не нашлась
                return Response({"status": "Call not accepted yet, finding car"})
        else:
            _id= instance.car_id_id 
            car_lat = CarsPosition.objects.get(car_id=_id).lat 
            car_long = CarsPosition.objects.get(car_id=_id).long
            current_car = CarsPosition.objects.get(car_id = instance.car_id_id)
            return Response({"car_lat": f"{car_lat}", "car_long": f"{car_long}"})






class CarsUpdate(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error" : "Method PUT not allowed"})
        try:
            instance = Cars.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarUpdateSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['is_working'] == True:
            return Response({"data":{"You are working"}},status=status.HTTP_200_OK)
        return Response({"data": {"You are not working"}}, status= status.HTTP_200_OK)


class CarGeoUpdate(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("id", None)
        if not pk:
            return Response({"error" : "Method PUT not allowed"})
        try:
            instance = CarsPosition.objects.get(car_id=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = CarGeoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
        
class SetCallArrived(APIView):
    def put(self, request, *args, **kwargs):
        id = kwargs.get("id", None)

        try:
            instance = Calls.objects.get(id=id)
        except:
            return Response({"error": "Object does not exists"})

        serializer = IsArrivedSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": f"Call {id} set as arrived"}, status=status.HTTP_200_OK)