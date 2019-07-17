from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views import generic
from .models import Donor
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


class SearchFormView(ListView):
    template_name = 'donors/donors_search.html'
    model = Donor
    success_url = '/donor_search/'
    def get_queryset(self):
        return Donor.objects.filter(hair_color=0)


# def donorsearch(request):
#     form = DonorSreachForm()
#     if request.method == 'GET':
#         return render_to_response(
#             'donors_search.html',{'form':form},RequestContext(request)
#         )
#     elif request.method == 'POST':
#         form = DonorSreachForm(request.POST)
#         donors = Donor.objects.all()
#         if form.is_valid():
#             donors = donor.filter(Q(hair_color_contains = form.cleaned_data['hair_color'])|Q(height_contains = form.cleaned_data['height']))
#             return render_to_response(
#                 'donor_search.html',
#                 {'form':form,'donors':donors},
#                 RequestContext(request)
#             )


# class SearchFormView(ListView):
#     paginate_by = 5
#     template_name = 'donors/donors_search.html'
#     model = Donor

#     # セッションに検索フォームの値を渡す
#     def donor(self,request,*args,**kwargs):
#         form_value = [
#             self.request.POST.get('hair_color',None)
#         ]
#         request.session['form_value'] = form_value

#         # 検索時にページネーションに関連したエラーを防ぐ
#         self.request.GET = self.request.GET.copy()
#         self.request.GET.clear()
        
#         return self.get(request, *args, **kwargs)


#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)

#         # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
#         hair_color = ''
#         if 'form_value' in self.request.session:
#             form_value = self.request.session['form_value']
#             hair_color = form_value[0]

#         default_data = {'hair _color':hair_color}

#         test_form = DonorSreachForm(initial=default_data) #検索データ
#         context['test_form'] = test_form

#         return context

#     def get_queryset(self):
#         # sessionに値がある場合、その値でクエリ発行する。
#         if 'form_value' in self.request.session:
#             form_value = self.request.session['form_value']
#             hair_color = form_value[0]

#             #検索条件
#             condition_hair_color = Q()

#             if len(hair_color) != 0 and hair_color[0]:
#                 condition_hair_color = Q(hair_color_icontains = hair_color)

#             return Donor.objects.select_related().filter(condition_hair_color)
#         else:
#             return Donor.objects.none()