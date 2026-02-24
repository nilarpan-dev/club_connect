from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Post

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_club_admin']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','caption']