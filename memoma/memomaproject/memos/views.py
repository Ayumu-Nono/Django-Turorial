from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import Memos
from .forms import MemosForm
# Create your views here.

class MemosHomeView(ListView):
    template_name = 'memos/home.html'
    model = Memos
    context_object_name = 'memo'



class MemoCreateView(CreateView):
    template_name = 'memos/create.html'
    model = Memos
    form_class = MemosForm
    success_url = '/memos/'