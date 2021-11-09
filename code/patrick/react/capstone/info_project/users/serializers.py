from rest_framework import serializers 
from rest_framework import serializers # imported serializers fror rest framework
from django.contrib.auth.models import User
from .models import Profile # added Model from model.py

#class for user serializer
class user_image_serializer(serializers.ModelSerializer):
    # meta class for all fields
    class Meta:
        model = Profile
        fields ='__all__'


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')