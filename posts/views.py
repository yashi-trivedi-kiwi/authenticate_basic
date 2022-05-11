from django.contrib import messages
from django.shortcuts import render, redirect

import constants
from posts.forms import AddPostForm
from posts.models import Post
from user_auth.forms import LoginForm


def front_view(request):
    """
    Creating a front view function for posts app where if user is authenticated
    rendering the first page as base.html template else redirecting to login view function to login
    :param request: wsgi request
    """

    if request.user.is_authenticated:
        return render(request, 'base.html')
    else:
        messages.error(request, constants.ERROR['not_logged_in']['need_login'])
        return redirect('login')


def is_active(request):
    """
    Creating an is_active function for filtering the active posts and rendering active_posts template
    :param request: wsgi request
    """
    post = Post.objects.filter(is_active=True)
    return render(request, 'active_posts.html', {'post': post})


def add_posts(request):
    """
    Creating add_posts function for adding new posts in form and then saving it,
    rendering post_temp template for showing added posts information
    :param request: wsgi request
    """
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            register = Post(title=title, description=description)
            register.save()
            form = AddPostForm()
    else:
        form = AddPostForm()
    return render(request, 'posts_temp.html', {'form': form})


def show_posts(request):
    """
    Created a show_posts function to view previous added post information,
    rendering it to show_posts.html which has the details of added posts
    :params request: wsgi request
    """
    post = Post.objects.all()
    return render(request, 'show_posts.html', {'post': post})


def edit(request, id):
    """
    Creating an edit function to update the posts information in tables
    with primary key as the ID of the post data, and then saving it to update the value
    :params request: wsgi request
    """
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        form = AddPostForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = Post.objects.get(pk=id)
        form = AddPostForm(instance=pi)
    return render(request, 'editpost.html', {'form': form})


def delete(request, id):
    """
    creating a delete function to delete the particular post with ID as the primary key
    after deleting, redirecting it to the same view function
    """
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
    return redirect('showpost')
