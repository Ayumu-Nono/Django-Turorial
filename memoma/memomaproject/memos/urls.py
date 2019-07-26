from django.urls import path,include
from . import views
from .views import MemosHomeView,MemoCreateView,MemoSearchView,MyPageView


app_name='memos'

urlpatterns = [
    path('',MemosHomeView.as_view(),name='home'),
    path('create/',MemoCreateView.as_view(),name='create'),
    path('search/',MemoSearchView.as_view(),name='search'),
    path('mypage/',MyPageView.as_view(),name='mypage'),
    ]
