from django.urls import path
from . import views

# app_name =
urlpatterns = [
    path('',views.todoView,name='main-view'),
    path('add/',views.addTodo,name='add-todo'),
    path('detail_todo/<int:id>',views.detail_todo,name='detail_todo')
]