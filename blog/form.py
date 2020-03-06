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


class ConfirmPasswordForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('password',)       
        widgets = {
            'password' : forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('password', 'Password does not match.')

    def save(self, commit=True):
        post = super(ConfirmPasswordForm, self).save(commit)
        if commit:
            post.save()
        return post