from django import forms

from .models import bookStore


class BookForm(forms.ModelForm):
    class Meta:
        model = bookStore
        fields = "__all__"
