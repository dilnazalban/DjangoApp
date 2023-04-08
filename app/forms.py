from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Rating


class ContactForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'insert'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'insert'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'insert'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', "last_name")

# class RatingForm(forms.ModelForm):
#     author = forms.HiddenInput(serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Rating
#         fields = ("__all__")
