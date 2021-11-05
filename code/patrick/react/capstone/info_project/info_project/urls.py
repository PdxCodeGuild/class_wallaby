from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from users.views import ProfileView, UpdateUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info_app.urls')),
    path('imageupload/', ProfileView.as_view(), name='users'),
    path('edituser/<int:pk>', UpdateUser.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('verify-email/',
    #      VerifyEmailView.as_view(), name='rest_verify_email'),
    # path('account-confirm-email/',
    #      VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
    #      VerifyEmailView.as_view(), name='account_confirm_email'),
    # path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

