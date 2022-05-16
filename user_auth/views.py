from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views import View

import constants
from .forms import RegisterForm, LoginForm


class register(View):

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)

    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request):
        """
        Creating a register function with get and post methods for getting values and
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
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                password2 = request.POST['password2']

                # check if Passwords Match
                if password == password2:
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
                            user.save()
                            messages.success(request, constants.SUCCESS['register_success']['success'])
                            return redirect('login')

                else:
                    messages.error(request, constants.ERROR['password']['do_not_match'])
                    return redirect('register')

            else:
                return render(request, 'register.html', context)


class login(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        """
                Creating a login class with a get and post function in it, where post method is
                authenticating with django user's authenticate method
                if user is authenticated , return redirecting to login
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
    form = LoginForm()
    context = {'form': form}
    auth.logout(request)
    messages.success(request, constants.SUCCESS['logout_success']['success'])
    return redirect('login')


# @login_required
class dashboard(View):
    """
    Creating a dashboard class with a get function in it,if user is authenticated
    after request passed, rendering it to dashboard template, else redirecting it to login page.
    :params request: wsgi request
    """

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'dashboard.html')
        else:
            messages.error(request, constants.ERROR['not_logged_in']['need_login'])
            return redirect('login')
