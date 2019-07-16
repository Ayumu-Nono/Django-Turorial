from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView

from .models import Donor
from .forms import DonorForms
 # Create your views here.


class DonorListView(ListView):
    template_name = 'donors/donors_list.html'
    model = Donor

class DonorCreateView(CreateView):
    template_name = 'donors/donors_create.html'
    model = Donor
    form_class = DonorForms
    success_url = '/donor/'


# class SearchFormView(CreateView):
#     template_name = 'data/donor_search.html'
#     model = DonorSearch
#     form_class = SearchForm
