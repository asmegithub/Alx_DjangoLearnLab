from taggit.models import Tag as TagBase
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from taggit.managers import TaggableManager


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Ensure no conflicting fields with 'tags' or 'tagged_posts'
    tags = TaggableManager()  # This should be the tag manager, not a direct field

    # def __str__(self):
    #     return self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')  # related_name is used to access comments from Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(TagBase):
    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    # Use a different related_name to avoid conflict
    posts = models.ManyToManyField(
        'blog.Post',
        related_name='tagged_posts',  # Changed from 'tags' to 'tagged_posts'
        blank=True
    )

    def __str__(self):
        return self.name
