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
    

   
    def get_context_data(self,**kwargs):
        context = super(DonorSearchedView,self).get_context_data(**kwargs)
        donors = self.model.objects.all()
        context['donors'] = donors

        default_data = {
        'number':6,
        'hair_color':2,
        'height':1,
        'weight':0,
        'ICI_IUI':0,
        'blood_type':6,
        'today_photo':1,
        'profile':1,
        'eye_color':2,
        'mot':3,
        }
        test_form = DonorSreachForm(initial=default_data)
        context['test_form']=test_form

        return context
 

    def get_queryset(self):
        object_list = self.model.objects.all()
        q_color = self.request.GET.get('color')
        q_height = self.request.GET.get('height')
        q_weight = self.request.GET.get('weight')
        q_ICI_IUI = self.request.GET.get('IUI_ICI')
        q_blood_type = self.request.GET.get('blood_type')
        q_today_photo = self.request.GET.get('today_photo')
        q_profile = self.request.GET.get('profile')
        q_eye_color = self.request.GET.get('eye_color')
        q_mot = self.request.GET.get('mot')       

        
        # object_list = object_list.filter(hair_color = q_color)
        # object_list = object_list.filter(height = q_height)
        # object_list = object_list.filter(weight = q_weight)
        # object_list = object_list.filter(ICI_IUI = q_ICI_IUI)
        # object_list = object_list.filter(blood_type = q_blood_type)
        # object_list = object_list.filter(today_photo = q_today_photo)
        # object_list = object_list.filter(profile = q_profile)
        # object_list = object_list.filter(eye_color = q_eye_color)
        # object_list = object_list.filter(mot = q_mot)
        object_list = object_list.filter(Q(mot = q_mot)|Q(hair_color = q_color))
        

                

        return object_list
        