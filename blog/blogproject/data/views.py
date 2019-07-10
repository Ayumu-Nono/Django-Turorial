from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

class DataList(generic.TemplateView):
    template_name='data/top.html'
