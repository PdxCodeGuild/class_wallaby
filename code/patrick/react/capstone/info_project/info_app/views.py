from django.shortcuts import redirect, render
import json
from requests.api import request
from django.http import JsonResponse
import xmltodict
import requests
from info_app.models import Feeds, UserSubscriptions, FeedName

from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from users.models import Profile
from django.db.models import Q
from django.views.generic import (
    ListView,
)
#-----------------------------------------------------
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
#-----------------------------------------------------
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics 
from .serializers import (
    FeedSerializer,
    UserSerializer, 
    UserSubscriptionsSerializer, 
    ProfileSerializer,  
    FeedNameSerializer, 
    ProfileSnipListSerializer,
    )
from rest_framework.permissions import IsAuthenticated


class SearchResultsView(ListView):
    model = Feeds
    queryset = Feeds.objects.order_by('-pubDate')
    template_name = 'info_app/search_results.html'
    

class Search(generics.ListCreateAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):  
        query = self.request.GET.get('q')
        object_list = Feeds.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) 
        )
        object_list = object_list.order_by('-pubDate')
        return object_list


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def addfeedsubs(request, format=None): 
    if request.method == 'GET':
        user_subscriptions = UserSubscriptions.objects.all()
        serializer = UserSubscriptionsSerializer(user_subscriptions, many=True, partial=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = UserSubscriptionsSerializer(data=request.data)      
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response ("user exists")


class SavedSnips(generics.ListAPIView):
    serializer_class = FeedSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Feeds.objects.filter(subscriber=user)


# Listview and create feeds
class Subscribe(generics.ListCreateAPIView):
    queryset = Feeds.objects.order_by('-pubDate')
    serializer_class = FeedSerializer

class UpdateSnipSubs(generics.RetrieveUpdateAPIView):
    queryset = Feeds.objects.order_by('-pubDate')
    serializer_class = FeedSerializer


class SubscribersUpdate(generics.RetrieveUpdateAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedSerializer

#Feed update subscriptions for UserSubscriptions model.
class UserSubscriptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionsSerializer

class FeedNameUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedName.objects.all()
    serializer_class = UserSubscriptionsSerializer

class FeedNameList(generics.ListCreateAPIView):
    queryset = FeedName.objects.all()
    serializer_class = FeedNameSerializer

def federalregister(request):
    data= requests.get('http://www.federalregister.gov/api/v1/documents.rss?&amp;conditions%5Bagency_ids%5D%5B%5D=466&amp;order=newest')
    response = data.text
    dict_data = xmltodict.parse(response)
    json_data = json.dumps(dict_data, indent=3)
    x= json.loads(json_data)
    results = x['rss']['channel']['item']
    for snip in results:
        try:
            title = snip['title']   
            description = snip['description']
            Date = snip['pubDate'].split(',')[1]
            Date1 = Date.split(' ')
            month_name = Date1[2]
            datetime_object = datetime.strptime(month_name, "%b")
            month_number = datetime_object.month
            pubDate = Date1[3]+'-'+str(month_number)+'-'+Date1[1]
            link = snip['link']
            data = Feeds(
                title=title,
                description=description,
                pubDate=pubDate,
                link=link,
                feed = 'federalregister',
            )
            data.save()
        except:
            print('unable to copy duplicate')
        return Response ("list Refreshed")
   






# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)



