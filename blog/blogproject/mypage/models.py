from django.db import models

class Mypage(models.Model):
    title = models.CharField(max_length=20,blank=False)
    detail = models.TextField(blank=False)