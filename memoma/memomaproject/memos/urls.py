from django.urls import path,include
from . import views
from .views import MemosHomeView,MemoCreateView


app_name='memos'

urlpatterns = [
    path('',MemosHomeView.as_view(),name='home'),
    path('create/',MemoCreateView.as_view(),name='create'),
    ]
