from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.utils.timezone import now



class Person(User):
    pass
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Device(models.Model):
    dname = models.CharField(max_length=30)
    dlocation = models.CharField(max_length=30)
    dkey = models.CharField(max_length=30,unique=True)
    downer = models.CharField(max_length=30)

class airstatus(models.Model):
    pm25 = models.IntegerField()
    pm10 = models.IntegerField()
    temperature = models.IntegerField()








    







