from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()
