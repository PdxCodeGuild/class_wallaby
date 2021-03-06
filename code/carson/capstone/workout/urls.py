from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/', views.event, name='event'),
    path('event/edit/(<event_id>)/', views.event, name='event_edit'),
    path('event/delete/<int:id>/', views.delete, name='event_delete'),
    path('record/', views.record, name='record'),
    path('api/diary/', views.diary_list),
 ]

