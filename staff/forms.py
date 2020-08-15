from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']

class CreateBlog(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
   