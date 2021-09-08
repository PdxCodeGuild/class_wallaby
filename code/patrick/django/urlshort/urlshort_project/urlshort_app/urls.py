from django.urls import path
from .views import  home, ShortCreateView, ShortUpdateView, ShortDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('short/add/', ShortCreateView.as_view(), name='short-add'),
    path('short/<int:pk>/', ShortUpdateView.as_view(), name='short-update'),
    path('short/<int:pk>/delete/', ShortDeleteView.as_view(), name='short-delete'),

]