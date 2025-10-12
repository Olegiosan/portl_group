from django.conf import settings
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="portf_liked_post", blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="portf_disliked_post", blank=True)

    def __str__(self):
        return "Портфоліо " + self.user.username

class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

class PortfolioFiles(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="files")
    files = models.FileField()