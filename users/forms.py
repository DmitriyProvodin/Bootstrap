from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'avatar', 'phone', 'country')
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
