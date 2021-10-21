from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    home, 
    federalregister,
    addfeedsubs,
    profilesniplist,
    test,
    
    FRList, 
    FRDetail, 
    Subscribe, 
    UserSubscriptions, 
    Subscribers,  
    FeedNameList, 
    FeedNameUpdate,
    SearchResultsView,
    SubscribersUpdate,
    Search, 
)

urlpatterns = [
    #home path
    path('', home, name='home'),

    #User snippet subscription
    path('profile/profilesniplist/<int:pk>', profilesniplist, name='profilesniplist'),
    path('profilesniplist/<int:pk>', profilesniplist, name='profilesniplist'),

    #Feed: post a new Feed user subscription or return a 404 to initiate an update.
    path('create/subscriptions', addfeedsubs, name='createsubscriptions'),

    #Feed user subscription updates
    path('feedsubs/<int:pk>', UserSubscriptions.as_view()),
    path('profile/feedsubs/<int:pk>', UserSubscriptions.as_view()),
    
    #Snippet subscription
    path('snipsubs/<int:pk>', Subscribers.as_view(), name='snipsubs'),
    path('search/snipsubs/<int:pk>', Subscribers.as_view(), name='snipsubs'),
    path('profile/snipsubs/<int:pk>', Subscribers.as_view()),
    path('profile/update/<int:pk>', SubscribersUpdate.as_view()),

    #list of all the feeds and details
    path('feed/all/', Subscribe.as_view()),
    path('profile/feed/all/', Subscribe.as_view()),
    
    
    #api to get data for the federal register, filtered for SEC
    path('federalregister', federalregister, name='federalregister'),
    
    
    
    #Profile views
    path('frapi/', FRList.as_view()),
    path('frapi/<int:pk>', FRDetail.as_view()),

    path('test/', test),
    

    #Feed Lists that exist
    path('feedlist', FeedNameList.as_view()),
    path('feedlistupdate', FeedNameUpdate.as_view()),

    #search
    path('search/api/', Search.as_view(), name='search_api'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]