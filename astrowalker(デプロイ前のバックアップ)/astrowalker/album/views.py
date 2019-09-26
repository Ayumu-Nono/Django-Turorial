from django.shortcuts import render
from .models import Image

def showall(reqest):
    images = Image.objects.all()
    context = {'images':images}
    return render(reqest,'album/showall.html',context)