from django.urls import path
from todo.views import todo_list, about

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('about', about, name='about'),
]
