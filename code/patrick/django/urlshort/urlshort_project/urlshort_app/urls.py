from django.urls import path
from .views import  home, ShortCreateView, ShortUpdateView, ShortDeleteView, URLDetailView

urlpatterns = [
    path('', home, name='home'),
    path('add/', ShortCreateView.as_view(), name='short-add'),
    path('<int:pk>/', ShortUpdateView.as_view(), name='short-update'),
    path('<int:pk>/delete/', ShortDeleteView.as_view(), name='short-delete'),
    path('url-detail/<int:pk>/', URLDetailView.as_view(), name='short-detail'),

]