from django.db import models


class AddBooks(models.Model):
    """
    Creating an AddBooks model with models.Model with fields
    as title,author_name,genre,price,date_created,date_modified
    """
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
