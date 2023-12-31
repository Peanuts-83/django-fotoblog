from django.db import models
from django.conf import settings
import os

class Photo(models.Model):
    image = models.ImageField(default="", max_length=256)
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    #  Delete file from hard-drive before db delete
    def delete(self, *args, **kwargs):
        if os.path.isfile(settings.MEDIA_ROOT + self.image.name):
            os.remove(settings.MEDIA_ROOT + self.image.name)
        super(Photo, self).delete(*args, **kwargs)

class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
