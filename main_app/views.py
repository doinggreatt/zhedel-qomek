from django.shortcuts import render
from rest_framework import generics, status
from .models import Calls, Clients, Medics, Cars, CarsPosition
from .serializer import ClientSerializer, CallSerializer, CallUpdateSerializer, CarUpdateSerializer, CarGeoSerializer, IsArrivedSerializer
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




class ClientCreate(APIView):
    def post(self, request):
        serializer=ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data_post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Clients.objects.get(pk=pk)
        except:
            return Response({"error":"Object does not exists"})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data_put": serializer.data})



class CallCreate(APIView):
    def post(self, request):
        request.data['client_phone'] = Clients.objects.get(id=request.data['client_id']).phoneNumber
        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data

        return Response({"data": {"status": "Call created and sent", "address":serializer.data['address']}}, status=status.HTTP_200_OK) 

    def put(self, request, *agrs, **kwargs):
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
            if nearest_car:
                distance = nearest_car['distance']
                instance.is_accepted=True
                instance.save()
                return Response({"status": "Your call accepted", "distance": distance})
            else:
                return Response({"status": "Call not accepted yet, finding car"})
        else:
            return Response({"status": "Call already accepted, car in the way!"})



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
        pk = kwargs.get("pk", None)
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