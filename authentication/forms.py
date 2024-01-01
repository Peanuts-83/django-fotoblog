from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User

class BaseForm(forms.Form):
    pass

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=63, label='User name')
    password = forms.CharField(min_length=8, max_length=63, label='Password', widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','firstname','lastname','role')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password','last_login','is_superuser','is_staff','date_joined','user_permissions','groups']