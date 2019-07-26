from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic
from .models import Donor,DonorSearch
from .forms import DonorForms,DonorSreachForm,MyForm

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
   
    def get_context_data(self,**kwargs):
       context = super(DonorSearchedView,self).get_context_data(**kwargs)
       donors = self.model.objects.all()
       context['donors'] = donors

       return context
 

    def get_queryset(self):
        object_list = self.model.objects.all()
        q_color = self.request.GET.get('color')
        color = 2
        object_list = object_list.filter(hair_color = q_color)

        return object_list
        