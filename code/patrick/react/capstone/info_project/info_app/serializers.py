from rest_framework import serializers 
from .models import Feeds, UserSubscriptions, FeedName
from users.models import Profile
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth.models import User
 
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = ('__all__')


class UserSubscriptionsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserSubscriptions
        fields = ('__all__')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')


class FeedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedName
        fields = ('__all__')
        

class ProfileSnipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Profile
        fields = ('__all__')

class UserSerializer(UserDetailsSerializer):

    profile = UserProfileSerializer(source="userprofile")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)

    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userprofile
        userprofile_data = validated_data.pop('userprofile', {})

        # to access the 'company_name' field in here
        # company_name = userprofile_data.get('company_name')   
        # profile_img = userprofile_data.get('image')                 
        # update the userprofile fields
        userprofile_serializer.update(userprofile_instance, userprofile_data)

        instance = super().update(instance, validated_data)
        print(instance)
        return instance            
            
    
