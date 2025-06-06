from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['name', 'description', 'price', 'image', 'available']