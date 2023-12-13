from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getBlogs(request):
    data = {
        "message": "Hello World",
    }
    return HttpResponse(data)
    
