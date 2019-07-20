from django.db import models
from django.utils import timezone

class Memos(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    title = models.TextField(max_length=20,null=False)
    sammary = models.TextField(max_length=100,null=False)
    slogan = models.TextField(max_length=20,null=False)
    fact = models.TextField(max_length=100,null=False)
    abstraction = models.TextField(max_length=100,null=False)
    diverse = models.TextField(max_length=100,null=False)