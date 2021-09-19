from django.urls import path
from .views import home, image_detail, download, ProfileDetailView, add_cart

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>', image_detail, name='detail'),
    path('download/<str:id>', download, name='download'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('add_cart/<int:id>', add_cart, name='add_cart'),

    
]