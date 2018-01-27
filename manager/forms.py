from django.contrib.auth.models import User
from django import forms
from .models import Carrier


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CarrierEditForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = ['name', 'register_date']