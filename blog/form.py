from django import forms
from .models import Post
from django.contrib.auth.hashers import check_password

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        widgets = {
            'password' : forms.PasswordInput(),
        }
        fields = ('title','text','password')
