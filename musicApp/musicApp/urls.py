from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('musicweb.urls')),
    path('api/', include('musicapi.urls')),
]
