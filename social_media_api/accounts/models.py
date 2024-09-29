from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    # please note that when ever u make a relationship, it's better to have a related_name argument to avoid conflicts!!
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='follower_users')
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='following_users')

    def __str__(self):
        return self.username
