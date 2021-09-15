from django.urls import path
from . import views

urlpatterns = [
  path('', views.root, name = 'root'),
  path('addurl/', views.addurl, name='addurl'),
  path('<str:shortUrl>/', views.surl_parse, name='surl_parse'),
]





