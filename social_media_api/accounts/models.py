from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField()
    profilePicture = models.CharField(max_length=255)
    followers = models.ManyToManyField('self', symmetrical=False)
