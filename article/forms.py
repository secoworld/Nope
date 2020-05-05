from django import forms
from comment.models import  Comment
from mdeditor.fields import MDTextFormField
from ckeditor.fields import RichTextFormField

class CommentForms(forms.ModelForm):
    context = MDTextFormField()
    aid = forms.IntegerField(label="文章id")
    parent_id = forms.IntegerField(label="父级评论id")

    class Meta:
        model = Comment
        fields = ["name", "email", 'context', 'aid', 'parent_id']