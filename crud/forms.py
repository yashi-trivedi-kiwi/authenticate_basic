from django import forms
from crud.models import AddBooks


class AddBooksForm(forms.ModelForm):
    """
    Creating books form with fields(title,author_name,genre,price,date_created,date_modified)
    from AddBooks model
    """

    class Meta:
        """
        class meta
        """
        model = AddBooks
        fields = ['title', 'author_name', 'genre', 'price']
