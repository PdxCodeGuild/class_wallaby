from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/products/', views.product_list),
    path('api/cart/<int:pk>', views.add_cart),
    path('api/products/<int:pk>', views.product_detail),
    path('', views.home, name='home'),
    path('cart/', views.get_cart, name= 'cart')
]

urlpatterns = format_suffix_patterns(urlpatterns)
