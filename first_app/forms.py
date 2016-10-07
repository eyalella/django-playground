from django import forms
from .models import Apartment


class AptForm(forms.ModelForm):
	class Meta:
		model = Apartment
		fields = ['location', 'price', 'size', 'image']


class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())
