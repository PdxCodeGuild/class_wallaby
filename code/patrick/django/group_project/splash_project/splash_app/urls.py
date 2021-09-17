from django.urls import path
from .views import home, image_detail

urlpatterns = [
    path('', home, name='home'),
    path('detail/<id>', image_detail, name='detail')
    
]