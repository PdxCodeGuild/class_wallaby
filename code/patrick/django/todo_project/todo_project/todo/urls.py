from django.urls import path
from . import views, PostDetailView

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('about', views.about, name='about'),
]
