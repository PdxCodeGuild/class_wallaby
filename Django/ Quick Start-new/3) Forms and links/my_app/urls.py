from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_blog_post, name = 'add_posts'),
    path('register/', views.register_author, name = 'register_author'),
    path('view_all/', views.view_all, name = 'view_all')
    ]