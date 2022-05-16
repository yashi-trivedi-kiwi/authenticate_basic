from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_view, name='frontview'),
    path('add', views.add_posts, name='addpost'),
    path('posts', views.show_posts, name='showpost'),
    path('update/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('active', views.is_active, name="is_active"),
]
