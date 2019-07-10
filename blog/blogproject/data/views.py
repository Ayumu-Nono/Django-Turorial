from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic

from .models import Donor
from .forms import DonorForms

class DataList(ListView):
    template_name='data/data.html'
    model = Donor #modelのなかのDonorモデルに登録されたデータを全て引っ張ってくる

class DonorCreate(CreateView):
    template_name = 'data/donor_create.html'
    model = Donor
    form_class = DonorForms
    success_url = '/data/' #記入したらここに戻ってくる



class Donor1(generic.TemplateView):
    template_name = 'data/donors/donor1.html'

class Donor2(generic.TemplateView):
    template_name = 'data/donors/donor2.html'

