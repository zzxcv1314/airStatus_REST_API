from django.contrib.auth.models import User, Group
from .models import Person
from .models import Device
from .models import airstatus
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.utils.crypto import get_random_string
import logging




class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = Device 
        fields = ('dname','dlocation','dkey','downer', 'id')
        setattr(Device, 'downer', User.username)
        print(getattr(Device,'downer'))
        #setattr(Device, 'dkey', 'testktey')

class AirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = airstatus
        fields = ('pm25', 'pm10', 'temperature','devicekey','id')
        



    



        