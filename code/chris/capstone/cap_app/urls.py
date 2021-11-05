from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('profile/', views.profile, name='profile'),
    path('reset/', views.reset, name='reset'),
    path('testPOST/', views.testPOST),
    path('answer/<str:answer_id>', views.answer, name='answer'),
    path('wrong/<str:answer_id>', views.wrong, name='incorrect'),
    path('stats/', views.stats, name='stats'),
]
