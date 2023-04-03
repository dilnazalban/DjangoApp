from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'insert'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'insert'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'insert'}))


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
