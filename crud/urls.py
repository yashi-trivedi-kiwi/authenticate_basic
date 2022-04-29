from django.contrib import admin
from django.urls import path, include

from crud import views

urlpatterns = [
    path('', views.addbooks, name="addbooks"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete")
]
