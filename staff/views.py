
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,CreateBlog
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from blog.models import Blog
# Create your views here.

def staff(request):
    if not request.user.is_authenticated:
        return redirect('staff:login')
    
    blogs = Blog.objects.filter(user=request.user)

    return render(request,'staff/staff.html',{'blogs':blogs})

def signup(request):
    if request.user.is_authenticated:
        return redirect('staff:staff')
    form = CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('staff:login')

    dicti = {'form':form}
    return render(request,'staff/signup.html', dicti)

@login_required(login_url='staff:login')
def change(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request,'staff/change.html',{'blogs':blogs})

def changeview(request,blog_id):
    
    blog = get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == 'GET':
        form = CreateBlog(instance=blog)
        return render(request,'staff/viewchanges.html',{'blog':blog,'form':form})
    else:
        form = CreateBlog(request.POST,request.FILES,instance=blog)
        form.save()
        return redirect('staff:staff')

def logina(request):
    if request.user.is_authenticated:
        return redirect('staff:staff')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
    
        if user is not None:
            login(request, user)
            return redirect('staff:staff')
        else:
            messages.error(request,'Username or password is incorrect. ')
            return render(request,'staff/login.html')

    return render(request,'staff/login.html')

def logouta(request):
    logout(request)
    return redirect('staff:login')

def create(request):
    form = CreateBlog()
    if request.method == 'POST':
        form = CreateBlog(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('blog:blog')
    blogs = {'form':form}
    return render(request,'staff/create.html',blogs)
