from django.urls import path
from django.conf.urls import url
from . import views

app_name='data'

urlpatterns = [
    path('',views.DataList.as_view(),name='top'),
    path('donor_create/',views.DonorCreate.as_view(),name='create'),
    path('donor_search/',views.SearchFormView.as_view(),name='search'),
    
]