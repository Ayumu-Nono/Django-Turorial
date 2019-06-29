from django.shortcuts import render
from django.views.generic import TemplateView

class MypageDataView(TemplateView):
    template_name = 'mypage/mypage_data.html'
