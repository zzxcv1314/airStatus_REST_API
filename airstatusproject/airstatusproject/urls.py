from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from airstatusapp import views
from rest_framework_extensions.routers import NestedRouterMixin

'''
# Create your views here.    

#defalut router를 사용한다. 
router = routers.DefaultRouter()
#router.register(r'accounts/signup', views.PersonSignupView)
router.register(r'devices', views.DeviceViewSet) #deviceviewset은 devices/ url로 연결하여 사용한다. 
router.register(r'airstatus', views.AirViewSet) #airviewset은 airstatus/ url로 연결하여 사용한다. 
urlpatterns = [
    url(r'^', include(router.urls)), 
    url(r'^account/',include('rest_auth.urls')), #rest-auth 는 account/ url로 연결하여 계정 관련 기능을 제공한다. 
    url(r'^account/signup/',include('rest_auth.registration.urls')) #rest-auth.registration 은 account/signup/ url로 연결하여 계정 관리 기능을 제공한다. 
    
]

'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('airstatusapp.urls')),
]





