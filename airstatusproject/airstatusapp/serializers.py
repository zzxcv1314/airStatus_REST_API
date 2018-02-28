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

#User에 관한 Serializer는 따로 설계하지 않았다. rest-auth에서 모두 제공한다. 


#Device Serializer 설계. 
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device #Device model을 사용한다.  
        fields = ('dname','dlocation','dkey','downer', 'id') #사용할 field 
        setattr(Device, 'downer', User.username) 
        #현재 로그인중인 User 의 username을 가져와 Device model의 downer field에 넣어준다. 
        #print(getattr(Device,'downer'))
        #setattr(Device, 'dkey', 'testktey')

        

#airstatus Serializer 설계 
class AirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = airstatus #airstatus model을 사용한다. 
        fields = ('pm25', 'pm10', 'temperature','devicekey','id') #사용할 field 
        



    



        