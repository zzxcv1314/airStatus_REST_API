from django.conf.urls import url, include
from rest_framework import routers
from airstatusapp import views
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter
from airstatusapp.views import DeviceViewSet
from airstatusapp.views import AirViewSet
# Create your views here.
class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()
#router.register(r'accounts/signup', views.PersonSignupView)
#router.register(r'devices', views.DeviceViewSet)
#router.register(r'airstatus', views.AirViewSet)

Device_router = router.register('Device', DeviceViewSet)
Device_router.register(
    'airstatus', AirViewSet,
    base_name='device-air',
    parents_query_lookups=['Device'])


urlpatterns = [
    url(r'^', include(router.urls)), 
    url(r'^account/',include('rest_auth.urls')),
    url(r'^account/signup/',include('rest_auth.registration.urls'))
    
]

