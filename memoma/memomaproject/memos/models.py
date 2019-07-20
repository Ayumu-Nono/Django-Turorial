from django.db import models
from django.utils import timezone

class Memos(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=20,null=False)
    sammary = models.CharField(max_length=100,null=False)
    slogan = models.CharField(max_length=20,null=False)
    fact = models.CharField(max_length=100,null=False)
    abstraction = models.CharField(max_length=100,null=False)
    diverse = models.CharField(max_length=100,null=False)