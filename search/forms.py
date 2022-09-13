from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Search

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
