from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"
    ROLE_CHOICES = ((CREATOR, "Créateur"), (SUBSCRIBER, "Abonné"))
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, null=True, blank=True)
    photo_profile = models.ImageField(
        verbose_name="Photo de profil", null=True, blank=True
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")
