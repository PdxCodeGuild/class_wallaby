from django.urls import path
from . views import TaskListForm, TaskListView, Update, Remove

urlpatterns = [
    path('', TaskListView, name='taskview'),
    path('form/', TaskListForm, name='taskform'),
    path('update/<int:id>', Update, name='update'),
    path('remove/<int:id>', Remove, name='remove'),
]