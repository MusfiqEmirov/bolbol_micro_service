from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT

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

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)