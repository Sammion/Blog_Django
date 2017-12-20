from django import forms
from .models import ArticleColumn, ArticleTag, ArticlePost, Comment


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ('tag',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title", "body")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator", "body")
