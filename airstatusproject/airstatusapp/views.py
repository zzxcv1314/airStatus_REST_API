#web으로 부터 요청 받을 view 파일. 
from django.contrib.auth.models import User, Group
from .models import Person
from .models import Device
from rest_framework import viewsets
from .serializers import DeviceSerializer
#from .serializers import PersonSerializer
#from .serializers import DeviceSerializer

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):
    
    #setattr(Device, 'dkey', 'testkey')
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    

