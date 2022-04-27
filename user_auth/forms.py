from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    """creating a register form with fields from auth user model"""
    password2 = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password','password2']


class LoginForm(forms.ModelForm):
    """
    creating a login form with fields from auth user model
    """
    class Meta:
        model = User
        fields = ['username', 'password']
