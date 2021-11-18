from django import forms
from django.forms.forms import Form
from django.forms.widgets import EmailInput


class SignInForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'id':'email',
            'class':'form-control',
            'placeholder':'Enter your email'
        })
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'id':'password',
            'class':'form-control',
            'placeholder':'Enter your password'
        })
    )

class SignUpForm(forms.Form):
    name = forms.CharField(
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'id':'name',
            'class':'form-control',
            'placeholder':'Enter your full name'

        })
    )
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'id':'email',
            'class':'form-control',
            'placeholder':'Enter your email'
        })
    )
    mobile = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'id':'mobile',
            'class':'form-control',
            'placeholder':'Enter your mobile no'
        })
    )
    password1 = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'id':'password1',
            'class':'form-control',
            'placeholder':'Enter your password'
        })
    )
    password2 = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'id':'password2',
            'class':'form-control',
            'placeholder':'Re-enter password'
        })
    )