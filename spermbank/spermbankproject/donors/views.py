from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic
from .models import Donor,DonorSearch
from .forms import DonorForms,DonorSreachForm

from django.db.models import Q
import logging

from django.template import RequestContext
from django.shortcuts import render_to_response
 # Create your views here.

logger = logging.getLogger('development')

class DonorListView(ListView):
    template_name = 'donors/donors_list.html'
    model = Donor

class DonorCreateView(CreateView):
    template_name = 'donors/donors_create.html'
    model = Donor
    form_class = DonorForms
    success_url = '/donor/'

class SearchFormView(CreateView):
    template_name = 'donors/donors_search.html'
    model = DonorSearch
    form_class = DonorSreachForm
    success_url = '/donor/'
    
class DonorSearchedView(ListView):
    template_name = 'donors/donors_searched_list.html'
    model = Donor
    color = 2
    def color_get_query(request):
        d = {
            'color':request.GET.get('color')
        }
        return render(request,'donor_searched_list.html',d)

    def get_queryset(self):
        color = 2
        return Donor.objects.filter(hair_color = 2)
