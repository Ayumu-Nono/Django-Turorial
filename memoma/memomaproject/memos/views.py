from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MemosHomeView(TemplateView):
    template_name = 'memos/home.html'


class MemoCreateView(TemplateView):
    template_name = 'memos/create.html'