from django.urls import path
from .views import  ShortListView, ShortCreateView, ShortUpdateView, ShortDeleteView, ShortDetailView

urlpatterns = [
    path('', ShortListView.as_view(), name='home'),
    path('add/', ShortCreateView.as_view(), name='short-add'),
    path('<int:pk>/', ShortUpdateView.as_view(), name='short-update'),
    path('<int:pk>/delete/', ShortDeleteView.as_view(), name='short-delete'),
    path('detail/<int:pk>/', ShortDetailView.as_view(), name='short-detail'),

]