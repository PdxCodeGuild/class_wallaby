from django.urls import path
from .views import home, image_detail, download

urlpatterns = [
    path('', home, name='home'),
    path('detail/<str:id>', image_detail, name='detail'),
    path('download/<str:id>', download, name='download')
    
]