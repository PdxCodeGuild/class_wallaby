from django.urls import path
# from .views import home, image_detail, download, ProfileDetailView, add_cart, user_orders, cart_view
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.image_detail, name='detail'),
    path('download/<str:id>', views.download, name='download'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('user_orders/', views.user_orders, name='user_orders'),
    path('cart/', views.cart_view, name='cart' ),
    # path('profile/', views.profile, name='profile'),
#    path('detail/', views.detail, name= 'detail')
    
]