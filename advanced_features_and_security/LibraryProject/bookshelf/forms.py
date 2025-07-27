from django import forms
from .models import Book


class BookSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100)
