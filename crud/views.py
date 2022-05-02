from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from crud.forms import AddBooksForm
from .models import AddBooks


def addbooks(request):
    """
    Adding data in forms in POST method and validating then saving it to database
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
            form = AddBooksForm()
    else:
        form = AddBooksForm()
    return render(request, 'add_books.html', {'form': form})


def show(request):
    books = AddBooks.objects.all()
    return render(request, 'show.html', {'book': books})


def update(request, id):
    if request.method == 'POST':
        pi = AddBooks.objects.get(pk=id)
        form = AddBooksForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = AddBooks.objects.get(pk=id)
        form = AddBooksForm(instance=pi)
    return render(request, 'update.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        pi = AddBooks.objects.get(pk=id)
        pi.delete()
    return redirect('show')
