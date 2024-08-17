
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken

app_name='api-v1'
urlpatterns=[
    #Registeration
    path('registeration/',views.RegistrationAPIView.as_view(),name='registeration'),

    #password-reset
    path('password-reset/',views.UpdatePassword.as_view(),name='password-reset'),

    #Token Authentication
    path(route='token/login', view=views.CustomAuthToken.as_view(),name='token-login'),
    path(route='token/logout', view=views.LogOutToken.as_view(),name='token-logout'),

    #JWT Authentication
    path('jwt/create/', views.CustomJwtPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]