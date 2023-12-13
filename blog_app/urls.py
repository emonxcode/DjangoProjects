from django.urls import path
from . import views

urlpatterns = [
    path('getBlogs/', views.getBlogs, name="getBlogs"),
]