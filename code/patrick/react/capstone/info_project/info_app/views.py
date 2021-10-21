from django.shortcuts import redirect, render
import json

from requests.api import request

import requests
from info_app.models import Feeds, UserSubscriptions, FeedName
import xmltodict
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from users.models import Profile
from django.db.models import Q
from django.views.generic import (
    ListView,
)
#-----------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics 
from .serializers import (
    FeedSerializer, 
    UserSubscriptionsSerializer, 
    ProfileSerializer,  
    FeedNameSerializer, 
    ProfileSnipListSerializer,
    )

# Home page rendering 
def home(request):
    x = Feeds.objects.all()
    return render(request, 'info_app/home.html')

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

from django.http import HttpResponse
 
def test(request):
    snips = Feeds.objects.filter(subscriber__id=1)
    for snip in snips:
        print(snip.pubDate)
    print(snips)
    return HttpResponse(request, "confirm")

#Profile snippet listview
@api_view(["GET", "PATCH"])
def profilesniplist(request, pk): 
    if request.method == 'GET':
        usersnips = Feeds.objects.filter(subscriber__id=pk)
        serializer = ProfileSnipListSerializer(usersnips, many=True)      
        return Response (serializer.data)


@api_view(["GET", "POST"])
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


# Listview and create feeds
class Subscribe(generics.ListCreateAPIView):
    queryset = Feeds.objects.order_by('-pubDate')
    serializer_class = FeedSerializer

class Subscribers(generics.RetrieveUpdateAPIView):
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


class FRList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FRDetail(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



#api to get xml data and convert it.
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
    
    contact_list = Feeds.objects.all()
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'info_app/federalregister.html', {'page_obj': page_obj})



    

