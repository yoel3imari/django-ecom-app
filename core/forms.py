from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
            'first_name': forms.TextInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
            'password1': forms.PasswordInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
            'password2': forms.PasswordInput(attrs={'class': 'py-2 px-6 rounded-xl block w-full'}),
        }