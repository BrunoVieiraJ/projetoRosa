# api/forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'idade']  # Substitua pelos campos do seu modelo
