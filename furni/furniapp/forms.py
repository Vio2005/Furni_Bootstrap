from django import forms
from .models import *




class ChairModelForm(forms.ModelForm):
    class Meta:
        model = Chair
        fields = ['name', 'price', 'photo']