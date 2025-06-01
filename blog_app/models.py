from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
