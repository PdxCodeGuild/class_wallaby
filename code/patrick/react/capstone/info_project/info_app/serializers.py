from rest_framework import serializers 
from .models import Feeds, UserSubscriptions, FeedName
from users.models import Profile
 
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
              
            
    
