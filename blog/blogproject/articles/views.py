from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView

from .models import Article
from .forms import ArticleForm

from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
from .models import Post



# class ArticleListView(ListView):
#     template_name = "articles/articles_list.html"
#     model = Article #modelにArticleを全部引っ張ってくる

# class ArticleCreateView(CreateView):
#     template_name = "articles/articles_create.html"
#     model = Article
#     form_class = ArticleForm
#     success_url = '/articles/'

    

class BaseListView(generic.ListView):
    paginate_by = 10
 
    def base_queryset(self):
        queryset = Post.objects.filter(
            is_publick=True).order_by('-created_at')
        return queryset
 
 
class PostIndexView(BaseListView):
    template_name='articles/post.html'

    def get_queryset(self):
        queryset = self.base_queryset()
        keyword = self.request.GET.get("quick")
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword))
 
        return queryset
 
 
class CategoryView(BaseListView):
    template_name='articles/side.html'
    
    def get_queryset(self):
        queryset = self.base_queryset()
        category = self.kwargs.get("small")
        if category:
            queryset = queryset.filter(category__name=category)
        else:
            category = self.kwargs.get("big")
            queryset = queryset.filter(category__parent__name=category)
 
        return queryset
 
 
class TagView(BaseListView):
 
    def get_queryset(self):
        tag = self.kwargs["tag"]
        queryset = self.base_queryset().filter(tag__name=tag)
        return queryset
 
 
class PostDetailView(generic.DetailView):
    model = Post
