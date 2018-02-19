from django.conf.urls import url, include
from rest_framework import routers
from airstatusapp import views
from rest_framework_extensions.routers import NestedRouterMixin


# Create your views here.

    

router = routers.DefaultRouter()
#router.register(r'accounts/signup', views.PersonSignupView)
router.register(r'devices', views.DeviceViewSet)
router.register(r'airstatus', views.AirViewSet)
urlpatterns = [
    url(r'^', include(router.urls)), 
    url(r'^account/',include('rest_auth.urls')),
    url(r'^account/signup/',include('rest_auth.registration.urls'))
    
]

