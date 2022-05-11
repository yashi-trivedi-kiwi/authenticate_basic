from django.db import models


class Post(models.Model):
    """
    Creating a model Post
    with fields 'title','description' and 'is_active'
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'posts'
