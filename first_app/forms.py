from django import forms
from .models import Apartment

class AptForm(forms.ModelForm):
  class Meta:
    model = Apartment
    fields = ['location', 'price', 'size', 'image']
