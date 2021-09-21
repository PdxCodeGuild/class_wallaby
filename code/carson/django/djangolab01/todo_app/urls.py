from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_note, name = 'add_posts'),
    path('register/', views.register_author, name = 'register_author'),
    path('view_all/', views.view_all, name = 'view_all'),
    path('post_details/<int:id>', views.post_details, name = 'details'),
    path('update_post/<int:id>', views.update_post, name = 'update_post'),
    path('delete_post/<int:id>', views.delete_post, name = 'delete_post')
]