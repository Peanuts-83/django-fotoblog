from django import forms
from . import models

class BaseForm(forms.Form):
    pass

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ('image','caption')