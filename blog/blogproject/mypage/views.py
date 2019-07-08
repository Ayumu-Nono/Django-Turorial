from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm

class Top(generic.TemplateView):
    template_name = 'mypage/top.html'

class MypageDataView(TemplateView):
    template_name = 'mypage/mypage_data.html'

class Login(LoginView):
    """ログインページ"""
    form_class=LoginForm
    template_name='mypage/login.html'

class Logout(LoginRequiredMixin,LogoutView):
    """"ログアウトページ"""
    template_name='mypage/top.html'