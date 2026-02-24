from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_club_admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)

class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('User', on_delete=models.CASCADE)