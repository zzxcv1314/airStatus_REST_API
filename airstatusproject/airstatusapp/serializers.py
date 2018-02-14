from django.contrib.auth.models import User, Group
from .models import Person
from .models import Device
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
        fields = ('dname','dlocation','dkey')
        #setattr(Device, 'dkey', 'testktey')




    



        