from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('', views.register.as_view(), name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard.as_view(), name='dashboard'),
]
