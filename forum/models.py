from xmlrpc.client import DateTime

from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_post", blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="disliked_post", blank=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_comment", blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="disliked_comment", blank=True)

    def __str__(self):
        return self.description

