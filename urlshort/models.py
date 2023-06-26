from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class urlShortener(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userurl', null=True)
    longurl = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=10,null=True)
    viewcount = models.IntegerField(default=0)

    def __str__(self):
        return self.shorturl