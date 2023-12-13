from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404



@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
def getPosts(request: Request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PUT":
        print("update")
    elif request.method == "DELETE":
        print("delete")
        
    
    
@api_view(http_method_names=["GET"]) 
def getPostById(request: Request, id: int):
    post = get_object_or_404(Post, id=id)
    
    serializer = PostSerializer(instance=post)
    
    return Response(data = serializer.data, status = status.HTTP_200_OK)