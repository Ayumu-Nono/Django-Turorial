from django.db import models
from django.utils import timezone
# from taggit.managers import TaggableManager

TAGS = (("0","内容がない"),("1","科学"),("2","思考"),("3","プログラミング"),("4","出来事"))

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField(blank=True)
    text = models.TextField(blank=False)
    date = models.DateTimeField(blank=False)
    photo = models.ImageField(upload_to='images/',default='defo_picture')
    sumnail = models.ImageField(upload_to='images/',default='defo_picture')
    tags = models.CharField(max_length=10,choices=TAGS,blank=True)
    # tags = models.ManyToManyField(Tag,blank=True)
    # tags = TaggableManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=20,blank=True)
    text = models.TextField()
    # target = models.ForeignKey(Post,on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

