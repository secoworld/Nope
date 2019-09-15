from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码", max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    next_page = forms.CharField(label="之前的页面", widget=forms.TextInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="密码", max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class':'form-control'}))
    next_page = forms.CharField(label="之前的页面", widget=forms.TextInput(attrs={'class':'form-control'}))