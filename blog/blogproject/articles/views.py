from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView

from .models import Article
from .forms import ArticleForm



class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    model = Article #modelにArticleを全部引っ張ってくる

class ArticleCreateView(CreateView):
    template_name = "articles/articles_create.html"
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

