from django.contrib import admin
from django.urls import path, include

from crud import views

urlpatterns = [
    path('/addbook', views.addbooks, name="addbooks"),
    path('update/<int:id>/', views.update, name="update"),
    path('deletebook/<int:id>/', views.deletebook, name="deletebook"),
    path('', views.show, name="show")
]
