from django.contrib import admin
from django.urls import path, include

from crud import views

urlpatterns = [
    path('', views.addbooks, name="addbooks"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('show', views.show, name="show")
]
