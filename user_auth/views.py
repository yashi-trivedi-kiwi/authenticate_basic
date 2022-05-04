from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
import constants
from .forms import RegisterForm, LoginForm


def register(request):
    """
    Creating a register form, and getting values
    Validating all fields with the  django default user methods
    Creating a user and saving the user
    Returning and redirecting to functions and templates for register form
    :param request: wsgi request
    """
    form = RegisterForm(request.POST or None)
    context = {'form': form}
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        if request.method == "POST":
            # Get form values
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            # check if Passwords Match
            if password == password2:
                # check Username
                if User.objects.filter(username=username).exists():
                    messages.error(request, constants.ERROR['username']['already_exists'])
                    if User.objects.filter(email=email).exists():
                        messages.error(request, constants.ERROR['email']['already_taken'])
                        return render(request, 'register.html', context)
                    return render(request, 'register.html', context)
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, constants.ERROR['email']['already_taken'])
                        return render(request, 'register.html', context)
                    else:
                        # Looks Good
                        user = User.objects.create_user(username=username, password=password,
                                                        email=email, first_name=first_name, last_name=last_name)
                        # Login After Register
                        # auth.login(request,user)
                        # messages.success(request,'You are now logged in.')
                        # return redirect('index')
                        user.save()
                        messages.success(request, constants.SUCCESS['register_success']['success'])
                        return redirect('login')

            else:
                messages.error(request, constants.ERROR['password']['do_not_match'])
                return redirect('register')

        else:
            return render(request, 'register.html', context)


def login(request):
    """
    Creating a login function
    authenticating with django user's authenticate method
    if user is authenticated , return to login page
    give message for login success
    else give message for invalid credentials
    :params request: wsgi request
    """
    form = LoginForm()
    context = {'form': form}

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, constants.SUCCESS['login_success']['success'])
                return redirect('dashboard')
            else:
                messages.error(request, constants.ERROR['invalid']['invalid'])
                return redirect('login')

        else:
            return render(request, 'login.html', context)


def logout(request):
    """
    Creating a logout function
    after logout request, redirecting it to login
    :params request: wsgi request
    """
    auth.logout(request)
    messages.success(request, constants.SUCCESS['logout_success']['success'])
    return redirect('login')


def dashboard(request):
    """
    Creating a dashboard function
    after request passed, rendering it to dashboard template
    :params request: wsgi request
    """
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

