from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path

from .views import (
    federalregister,
    addfeedsubs,
    
    Subscribe, 
    UserSubscriptions, 
    UpdateSnipSubs,  
    FeedNameList, 
    FeedNameUpdate,
    SearchResultsView,
    Search, 
    SavedSnips
)

urlpatterns = [
    #Feed: post a new Feed user subscription or return a 404 to initiate an update.
    path('create/subscriptions', addfeedsubs, name='createsubscriptions'),

    #Feed user subscription updates
    path('feedsubs/<int:pk>', UserSubscriptions.as_view()),
    
    #Snippet subscription
    path('snipsubs/<int:pk>', UpdateSnipSubs.as_view(), name='snipsubs'),

    #list of all the feeds and details
    path('feed/all/', Subscribe.as_view()),
    
    #api to get data for the federal register, filtered for SEC
    path('federalregister/', federalregister, name='federalregister'),
    
    #snips saved by user
    path('savedsnips/', SavedSnips.as_view()),

    #Feed Lists that exist
    path('feedlist/', FeedNameList.as_view()),
    path('feedlistupdate/', FeedNameUpdate.as_view()),

    #search
    path('search/api/', Search.as_view(), name='search_api'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]