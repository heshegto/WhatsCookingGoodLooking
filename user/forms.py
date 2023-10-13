from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)
from user.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'type': "username",
        'placeholder': 'Name',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form__input',
        'type': "password",
        'placeholder': 'Password',
    }))

    class Meta:
        model = User
        fields = ("username", 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': "form__input",
        'type': "text",
        'placeholder': "Name",
    }))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class': "form__input",
        'type': "text",
        'placeholder': "Email",
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form__input",
        'type': "password",
        'placeholder': "Password",
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form__input",
        'type': "password",
        'placeholder': "Confirm password",
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
