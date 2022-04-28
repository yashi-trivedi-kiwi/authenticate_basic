from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    """
    Creating a register form with fields(first_name,last_name,username,password) from auth user model

    """
    password2 = forms.CharField(max_length=100)

    class Meta:
        """
        class meta
        """

        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']


class LoginForm(forms.ModelForm):
    """
    Creating a login form with fields(username, password) from auth user model
    """
    class Meta:
        model = User
        fields = ['username', 'password']
