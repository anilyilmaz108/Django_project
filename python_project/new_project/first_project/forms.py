from django import forms
from .models import posts

class ListForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ["title","description","date"]