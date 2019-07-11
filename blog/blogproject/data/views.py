from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic
from django.http import HttpResponse

from .models import Donor,DonorSearch
from .forms import DonorForms,SearchForm



class DataList(ListView):
    template_name='data/data.html'
    model = Donor #modelのなかのDonorモデルに登録されたデータを全て引っ張ってくる

class DonorCreate(CreateView):
    template_name = 'data/donor_create.html'
    model = Donor
    form_class = DonorForms
    success_url = '/data/' #記入したらここに戻ってくる


class SearchFormView(CreateView):
    template_name = 'data/donor_search.html'
    # model = DonorSearch
    form_class = SearchForm


def search(request):
    f = SearchForm({
        'name':'なまえ'
    })
    return render(
        request,
        'donor_search.html',
        {'form1':f}
    )



class Donor1(generic.TemplateView):
    template_name = 'data/donors/donor1.html'

class Donor2(generic.TemplateView):
    template_name = 'data/donors/donor2.html'

