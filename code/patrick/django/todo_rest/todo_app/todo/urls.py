from django.urls import path
from . views import TaskListForm, TaskListView, Update, Remove, TodoAPI

urlpatterns = [
    path('', TaskListView, name='taskview'),
    path('form/', TaskListForm, name='taskform'),
    path('update/<int:id>', Update, name='update'),
    path('remove/<int:id>', Remove, name='remove'),
    path('api/', TodoAPI.as_view())
]