from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import bookStore, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = bookStore
        fields = "__all__"
        exclude = ("isbn",)

    def clean(self):
        super(BookForm, self).clean()
        description = self.cleaned_data.get("description")
        title = self.cleaned_data.get("title")
        if len(description) < 10:
            raise ValidationError("content must be bigger than 2 chars")
        if len(title) < 10:
            raise ValidationError("Title must be more than 10 chars")
        if len(title) > 50:
            raise ValidationError("Title must be less than 50 chars")

        return self.cleaned_data


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean(self):
        super(CatForm, self).clean()
        name = self.cleaned_data.get("name")

        if len(name) < 2:
            raise ValidationError("content must be bigger than 2 chars")

        return self.cleaned_data


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user