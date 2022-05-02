from django import forms
from crud.models import AddBooks


class AddBooksForm(forms.ModelForm):
    """
    Creating books form with fields(title,author_name,genre,price) from Books model
    """

    class Meta:
        """
        class meta
        """
        model = AddBooks
        fields = ['title', 'author_name', 'genre', 'price']
