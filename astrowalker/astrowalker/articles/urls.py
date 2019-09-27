from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import ArticleListView,ArticleDetailView,PostArchiveView,TagSearchedListView

app_name = 'articles'
urlpatterns = [
    path('',ArticleListView.as_view(),name='article.list'),
    path('<int:pk>/',ArticleDetailView.as_view(),name='article'),
    path('archive/',PostArchiveView.as_view(),name='post_archive'),
]
