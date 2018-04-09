from django import forms
from .models import *
from categories.models import *

class CategorySearchForm(forms.Form):
    category = forms.CharField(required=False)