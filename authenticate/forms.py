from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    password= forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email','password',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
