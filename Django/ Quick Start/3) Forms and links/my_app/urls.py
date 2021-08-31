from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.add_blog_post, name = 'posts'),
    path('register/', views.register_author, name = 'register_author')
]