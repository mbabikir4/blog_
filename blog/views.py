from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.

def blogs(request):
    blogs = Blog.objects.all().order_by('-time')
    return render(request,'blog/blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
