from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import Memos
from .forms import MemosForm
# Create your views here.

class MemosHomeView(TemplateView):
    template_name = 'memos/home.html'


class MemoCreateView(CreateView):
    template_name = 'memos/create.html'
    model = Memos
    form_class = MemosForm
    success_url = '/memos/'