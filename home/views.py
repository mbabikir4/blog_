from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home/index.html',{'blogs':blogs})

