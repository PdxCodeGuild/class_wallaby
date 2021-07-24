from django.urls import path, include #'include' is used to allow connection between multiple urls.py routes
from . import views

# urlpatterns = [path('', views.index, name='index'), 
#                path('posts/',views.posts, name='posts'),]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('base/<str:id>/', views.base_capture),
    path('base/wont_match/', views.base_wont_match),  # this will never match because of _both_ of above routes.
]