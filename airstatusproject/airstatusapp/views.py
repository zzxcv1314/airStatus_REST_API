#web으로 부터 요청 받을 view 파일. 
from django.contrib.auth.models import User, Group
from .models import Person
from .models import Device
from .models import airstatus
from rest_framework import viewsets
from .serializers import DeviceSerializer
from .serializers import AirSerializer
import uuid 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import generics

#from .serializers import PersonSerializer
#from .serializers import DeviceSerializer

# Create your views here.


class DeviceViewSet(viewsets.ModelViewSet):
    
    #setattr(Device, 'dkey', 'testkey')
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend,)
    
    filter_fields = ('dname',)
    def perform_create(self, serializer):
        #serializer.save(dkey = 'abcd')
        serializer.save(downer = str(self.request.user))

class AirViewSet(viewsets.ModelViewSet):
    queryset = airstatus.objects.all()
    serializer_class =  AirSerializer
    
