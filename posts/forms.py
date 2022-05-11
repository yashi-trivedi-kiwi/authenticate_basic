from django import forms
from posts.models import Post


class AddPostForm(forms.ModelForm):
    """
    Creating AddPost form with fields(title,description) from Post model
    """

    class Meta:
        """
        class meta
        """
        model = Post
        fields = ['title', 'description']
