from django.urls import path, include
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
    'admin/',
    admin.site.urls
    ),
    
    path(
    "api/v1/",
    include("users.urls")
    ),
    
    #jwt
    path(
    'api/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair'
    ),  # Token almaq üçün
    
    path(
    'api/token/refresh/', TokenRefreshView.as_view(),
    name='token_refresh'
    ),  # Token yeniləmək üçün
]

