from rest_framework import serializers 
from rest_framework import serializers # imported serializers fror rest framework

from .models import Profile # added Model from model.py

#class for krisi_user serializer
class user_image_serializer(serializers.ModelSerializer):
    # meta class for field which we want to show
    class Meta:
        model = Profile
        fields ='__all__'