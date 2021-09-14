from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('shorten/', views.shorten_url, name = 'shorten'),
   
]