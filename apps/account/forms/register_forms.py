from django import forms
from django.core.exceptions import ValidationError
import re

from apps.account.validators import validate_alpha, validate_password_strength


class RegisterForm(forms.Form):
    firstname = forms.CharField(
        max_length=50,
        required=True,
        label="Prenom",
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Prenom',
                'class': 'form-control'
            }
        )
    )

    lastname = forms.CharField(
        max_length=50,
        required=True,
        label="Nom",
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": 'form-control'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label="Mot de passe",
        validators=[validate_password_strength],
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe",
                "class": 'form-control'
            }
        )
    )

    confirm_password = forms.CharField(
        required=True,
        label=" Confirmer le Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmer le Mot de passe",
                "class": 'form-control'
            }
        )
    )




