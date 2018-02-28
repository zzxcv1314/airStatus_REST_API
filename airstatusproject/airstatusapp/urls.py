from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers



router = DefaultRouter()
#router.register(r'devices', views.DeviceViewSet)
router.register(r'airstatus', views.AirViewSet)
router.register(r'devices', views.DeviceViewSet)
#router.register(r'create', views.DeviceCreateViewSet, base_name='devices')





urlpatterns = [ 

    url(r'^main', views.main, name='main'),
    url(r'^menu', views.menu, name="menu"),
    
    url(r'^devicesview', views.devicesview, name='devicesview'),
    #url(r'^devicecreate', views.devicecreate, name='devicecreate')
    
    
    
    #url(r'^devices/create', device_create, name ='device_create' )

]

urlpatterns += router.urls