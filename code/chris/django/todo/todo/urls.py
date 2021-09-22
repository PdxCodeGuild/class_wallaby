from django.urls import path
from . import views

urlpatterns = [
  path('', views.root, name = 'root'),
  path('<int:todo_id>/edit', views.edit_todo, name='edit'),
  path('<int:todo_id>/complete', views.edit_complete, name='complete'),
  path('<int:todo_id>/delete', views.delete, name='delete'),
  path('<int:todo_id>/', views.detail, name='detail'),
  path('add_todo/', views.add_todo, name='add_todo'),
]