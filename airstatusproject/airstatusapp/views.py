#web으로 부터 요청 받을 view 파일. 
from django.contrib.auth.models import User, Group
from .models import Person
from .models import Device
from .models import airstatus
from rest_framework.viewsets import ModelViewSet
from .serializers import DeviceSerializer
from .serializers import AirSerializer
import uuid 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework_extensions.mixins import NestedViewSetMixin

#from .serializers import PersonSerializer
#from .serializers import DeviceSerializer

#user에 관한 Viewset은 설계하지 않는다. rest auth 제공 viewset사용

#device viewset 
class DeviceViewSet(NestedViewSetMixin, ModelViewSet):
    
    #setattr(Device, 'dkey', 'testkey')
    queryset = Device.objects.all() #device의 모든 object를 사용한다. 
    serializer_class = DeviceSerializer #설계해둔 Deiveserializer를 사용한다. 
    filter_backends = (DjangoFilterBackend,) #url filtering을 위한 framework
    filter_fields = ('dname', 'downer', 'dlocation', 'id',) 
    #filtering 시 사용할 field들

    def perform_create(self, serializer):
        #serializer.save(dkey = 'abcd')
        serializer.save(downer = str(self.request.user))
        #ViewSet이 실행되면 downer에 현재 username을 저장한다. 

#airstatus viewset 
class AirViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = airstatus.objects.all() #airstatus의 모든 object를 사용한다. 
    serializer_class =  AirSerializer #설계해둔 airserializer를 사용한다. 
    filter_backends = (DjangoFilterBackend,) #url filtering을 위한 framework
    filter_fields = ('devicekey', 'pm25','pm10','temperature','id',)
    #filtering시 사용할 field들. 
    
