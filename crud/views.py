from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

import constants
from crud.forms import AddBooksForm
from .models import AddBooks
from django.contrib import messages


def addbooks(request):
    """
    Adding data in forms in POST method and validating then saving it to database
    :params request: wsgi request
    """
    if request.method == 'POST':
        form = AddBooksForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            author_name = request.POST['author_name']
            genre = request.POST['genre']
            price = request.POST['price']
            register = AddBooks(author_name=author_name, title=title, genre=genre, price=price)
            register.save()
            messages.success(request, constants.SUCCESS['added_books']['success'])
            form = AddBooksForm()
    else:
        form = AddBooksForm()
    return render(request, 'add_books.html', {'form': form})


def show(request):
    """
    Created a show function to view previous added books information
    :params request: wsgi request
    """
    if request.user.is_authenticated:
        books = AddBooks.objects.all()
        return render(request, 'show.html', {'book': books})
    else:
        messages.error(request, constants.ERROR['not_logged_in']['need_login'])
        return redirect('login')


def update(request, id):
    """
    Creating an update function to update the books information in tables
    with primary key as the ID of the book data, and then saving it to update the value
    :params request: wsgi request
    """
    if request.method == 'POST':
        pi = AddBooks.objects.get(pk=id)
        form = AddBooksForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = AddBooks.objects.get(pk=id)
        form = AddBooksForm(instance=pi)
    return render(request, 'editbook.html', {'form': form})


def deletebook(request, id):
    """
    creating a deletebook function to delete the particular book with ID as the primary key
    after deleting, redirecting it to the same view function
    """
    if request.method == 'POST':
        pi = AddBooks.objects.get(pk=id)
        pi.delete()
    return redirect('show')
