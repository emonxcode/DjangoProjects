from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post, name="post_list"),
    path('post/<int:id>', views.getPostById, name="post_details"),
    path('post/update/<int:id>', views.postOperation, name="update_post"),
    path('post/delete/<int:id>', views.postOperation, name="delete_post"),
]