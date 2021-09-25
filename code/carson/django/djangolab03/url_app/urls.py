from django.urls import path
from . import views
urlpatterns = [
    path('shorten/', views.shorten_url, name = 'shorten'),
   
]