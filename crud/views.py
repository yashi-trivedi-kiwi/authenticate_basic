from django.shortcuts import render

from crud.forms import AddBooksForm
from .models import AddBooks


def addbooks(request):
    """
    Adding data in forms in POST method and validating then saving it to database
    """
    if request.method == 'POST':
        form = AddBooksForm()
        if form.is_valid():
            title = form.cleaned_data['title']
            author_name = form.cleaned_data['author_name']
            genre = form.cleaned_data['genre']
            price = form.cleaned_data['price']
            register = AddBooks(author_name=author_name, title=title, genre=genre, price=price)
            register.save()
            form = AddBooksForm()
    else:
        form = AddBooksForm()

    books = AddBooks.objects.all()
    return render(request, 'add_books.html', {'form': form, 'book': books})


def update(request):
    pass


def delete(request):
    pass
