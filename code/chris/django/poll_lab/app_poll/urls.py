from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('poll/', views.poll, name = 'poll'),
    path('poll/<int:question_id>/', views.detail, name = 'detail'),
    path('poll/<int:question_id>/results/', views.results, name = 'results'),
    path('poll/<int:question_id>/vote/', views.vote, name = 'vote'),

]
