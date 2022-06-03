from django.forms import ModelForm
from django import forms
from .models import blog


class BlogForm(forms.ModelForm):
    title = forms.CharField()
    intro = forms.CharField(widget=forms.Textarea)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

    class Meta:
        model = blog
        fields = ['title', 'intro', 'body', 'image']
