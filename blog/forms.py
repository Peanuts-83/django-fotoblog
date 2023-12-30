from django import forms
from . import models
from authentication import models as authModel

class BaseForm(forms.Form):
    pass

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ('image','caption')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = authModel.User
        exclude = ['password','last_login','is_superuser','is_staff','date_joined','user_permissions','groups']