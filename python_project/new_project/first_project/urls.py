from django.urls import path 
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('posts/', views.postt, name="posts"),
    path('create/', views.create, name="create"),
    path('delete/<posts_id>', views.delete, name="delete"),
    path('update/<posts_id>', views.update, name="update"),
]
