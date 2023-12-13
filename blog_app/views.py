from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404



@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
def post(request: Request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
         
        response = {
        "message": "Success",
        "data": serializer.data
         }
        
        return Response(data = response, status = status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            
            response = {
                "message": "Saved",
                "data": serializer.data
            }
            
            return Response(data = response, status = status.HTTP_200_OK)
        else:
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
    
    
@api_view(http_method_names=["GET"]) 
def getPostById(request: Request, id: int):
    post = get_object_or_404(Post, id=id)
    
    serializer = PostSerializer(instance=post)
    
    response = {
        "message": "Success",
        "data": serializer.data
    }
    
    return Response(data = response, status = status.HTTP_200_OK)


@api_view(http_method_names=["PUT", "DELETE"])
def postOperation(request: Request, id: int):
    if request.method == "PUT":
        post = get_object_or_404(Post, id=id)

        data = request.data

        serializer = PostSerializer(instance=post, data=data)

        if(serializer.is_valid()):
            serializer.save()
            response = {
                "message": "Updated",
                "data": serializer.data
            }
            return Response(data = response, status = status.HTTP_200_OK)
        else:
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
    elif request.method == "DELETE":
        post = get_object_or_404(Post, id=id)
        
        post.delete()
        return Response(data={"message": "Deleted"}, status = status.HTTP_204_NO_CONTENT)