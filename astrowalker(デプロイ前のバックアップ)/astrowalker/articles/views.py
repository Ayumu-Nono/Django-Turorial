from django.shortcuts import render
from .models import Post,Comment,Tag
from django.views.generic import ListView,DetailView,ArchiveIndexView
# from taggit.models import Tag
from django.template import RequestContext
from django.shortcuts import render_to_response


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    model = Post
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super(ArticleListView,self).get_context_data(**kwargs)
        post = self.model.objects.all()
        context['post'] = post

        default_data  = {
            'tags':0
        }
        return context

    def get_queryset(self):
        object_list = self.model.objects.all().order_by('-date')
        q_tags = self.request.GET.get('tags')
        # q_tags = 4
        if q_tags is not None:
            if q_tags != "":
                object_list = object_list.filter(tags=q_tags)
        return object_list

class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    model = Post
    context_object_name = 'article'

class PostArchiveView(ArchiveIndexView):
    model = Post
    date_field = 'date'
    allow_empty = True

class TagSearchedListView(ListView):
    template_name = 'articles/post_tagsearched.html'
    model = Post