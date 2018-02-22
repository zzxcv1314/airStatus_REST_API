from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.utils.timezone import now
import uuid

#model 설계에 필요

#person model 설계, User를 상속받는다. 
class Person(User):
    pass
    #User model을 그대로 사용. 
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
#person이 생성되면 Token생성한다. 

#Device model 설계
class Device(models.Model):
    dname = models.CharField(max_length=30)
    dlocation = models.CharField(max_length=30)
    dkey = models.UUIDField(primary_key=True, default = uuid.uuid1, editable =False)
    #dkey를 primary키로 사용한다. 
    downer = models.CharField(max_length=30, editable=False)
    #non-editable하게 설계한다. 현재 로그인중인 사용자의 ID값이 들어가게 됨. 

#airstatus model 설계     
class airstatus(models.Model):
    pm25 = models.CharField(max_length=30)
    pm10 = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    devicekey = models.CharField(max_length=60, null=True)
    #URL에 포함된 devicekey의 정보를 가져와서 저장한다. 








    







