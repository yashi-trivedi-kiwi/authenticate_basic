from django.db import models


class AddBooks(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
