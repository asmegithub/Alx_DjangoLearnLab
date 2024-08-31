from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, date_of_birth, profile_photo):
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, date_of_birth, profile_photo):
        user = self.create_user(
            username, password, date_of_birth, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)

    REQUIRED_FIELDS = ['date_of_birth', 'profile_photo']

    objects = CustomUserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"title= {self.title} author= {self.author} publication year= {self.publication_year}"
