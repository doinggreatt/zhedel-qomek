from django.shortcuts import render
from rest_framework import generics, status
from .models import Calls, Clients, Medics, Cars
from .serializer import ClientSerializer, CallSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import redis, json
from zhedel_qomek import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.forms import model_to_dict
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)


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


class CalcAddress():
    def __init__(self, lat, long):
        print(lat, long)

class CallCreate(APIView):
    def post(self, request):
        request.data['client_phone'] = Clients.objects.get(id=request.data['client_id']).phoneNumber
        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response({"data": {"address":serializer.data['address']}}, status=status.HTTP_200_OK)