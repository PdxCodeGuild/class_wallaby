from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('cart/', views.cart, name = 'cart'),

]
# urlpatterns = [
    
#      path('download/<str:id>', download, name='download'),
#      path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
#     path('add_cart/<id>', add_cart, name='add_cart'),

# ]