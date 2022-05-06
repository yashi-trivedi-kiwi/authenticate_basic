from django.shortcuts import render

from posts.models import Post


def listing(request, is_active):
    if not is_active:
        listings = Post.objects.filter(is_active=True)
