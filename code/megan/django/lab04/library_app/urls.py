from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('all_books/', views.all_books, name = 'all_books'),
    path('check_out_in/', views.check_out_in, name = 'check_out_in'), 
    path('details/<int:id>', views.details, name = 'details'),
]