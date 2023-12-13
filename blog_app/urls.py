from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.getPosts, name="post_list"),
    path('post/<int:id>', views.getPostById, name="post_details"),
]