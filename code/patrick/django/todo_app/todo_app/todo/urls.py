from django.urls import path
from . views import TaskListForm, TaskListView, DetailView

urlpatterns = [
    path('', TaskListView, name='taskview'),
    path('form/', TaskListForm, name='taskform'),
    path('detail/<int:id>', DetailView, name='detailview'),
]