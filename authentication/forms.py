from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User
from django.template.loader import render_to_string

class BaseForm(forms.Form):
    pass

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=63, label="User name")
    password = forms.CharField(
        min_length=8, max_length=63, label="Password", widget=forms.PasswordInput
    )

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "firstname", "lastname", "role")

# customInputField for photo_profile input in ProfileForm
class CustomPhotoInput(forms.ClearableFileInput):
    template_name = 'auth/custom-photo-input.html'
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs['onchange'] = "doUpdatePhoto(event)"
        substitutions = {
            'input': super().render(name, value, attrs, renderer),
            'clear_checkbox_label': '',
            'value': value if value else None,
            'widget': self
        }
        template = self.template_name
        result = render_to_string(template, substitutions)
        return result

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "date_joined",
            "user_permissions",
            "groups",
            "id_photo_profile"
        ]
        widgets = {
            "photo_profile": CustomPhotoInput()
        }
