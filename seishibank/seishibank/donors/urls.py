from django.urls import path,include
from .views import DonorListView ,DonorCreateView


urlpatterns = [
    path('',DonorListView.as_view(),name='donors.list'),
    path('create/',DonorCreateView.as_view(),name='donors.create'),
]
