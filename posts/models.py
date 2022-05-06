from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
