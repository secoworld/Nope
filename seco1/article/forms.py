from django import forms
from comment.models import  Comment
from mdeditor.fields import MDTextFormField

class CommentForms(forms.ModelForm):
    context = MDTextFormField()

    class Meta:
        model = Comment
        fields = ['context',]