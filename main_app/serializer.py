from rest_framework import serializers
from .models import Calls, Clients, Medics

class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls 
        fields='__all__'

        
class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients 
        fields = '__all__'
class MedicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medics 
        fields = '__all__'