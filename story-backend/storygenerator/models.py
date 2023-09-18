
from django.db import models

class Story(models.Model):
    prompt = models.TextField()
    content = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)

class UserPrompt(models.Model):
    prompt = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
