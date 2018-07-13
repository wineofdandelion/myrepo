from django.forms import ModelForm
from . import models


class CommentForm(ModelForm):
    class Meta():
        model = models.Comment
        fields = ["comment_text"]
