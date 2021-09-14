from django.urls import path
from . import views

urlpatterns = [
  path('', views.root, name = 'root'),
  path('s/<str:surl>/', views.surl_parse, name='surl_parse'),
]
