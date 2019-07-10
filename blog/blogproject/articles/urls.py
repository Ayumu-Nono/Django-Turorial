from django.urls import path
from django.conf.urls import u
from . import views
from django.views.generic  import TemplateView

app_name='articles'

urlpatterns = [
    path('', views.Top.as_view(), name='index'),
    # path('detail/',views.PostDetailView.as_view(), name='detail'),
    # path('category/',views.CategoryView.as_view(), name='category'),
    # path('category/',views.CategoryView.as_view(), name='category'),
    # path('tag/',views.TagView.as_view(), name='tag'),
]
