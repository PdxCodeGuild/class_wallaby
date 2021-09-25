from django.urls import path
from .views import home, image_detail, download, ProfileDetailView, add_cart, user_orders, cart_view

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>', image_detail, name='detail'),
    path('download/<str:id>', download, name='download'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('add_cart/<int:id>', add_cart, name='add_cart'),
    path('user_orders/', user_orders, name='user_orders'),
    path('cart/', cart_view, name='cart' ), 
    
   

    
]