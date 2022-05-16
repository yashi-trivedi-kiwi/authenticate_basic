from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth.urls')),
    path('crud/', include('crud.urls')),
    path('posts/', include('posts.urls')),
]
