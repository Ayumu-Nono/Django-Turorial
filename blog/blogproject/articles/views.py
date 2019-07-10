from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView

from .models import Article
from .forms import ArticleForm

from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
from .models import Post



class Top(generic.TemplateView):
    template_name = 'article/top.html'
    