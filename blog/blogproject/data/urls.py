from django.urls import path
from . import views

app_name='data'

urlpatterns = [
    path('',views.DataList.as_view(),name='top'),
    path('donor_create/',views.DonorCreate.as_view(),name='create'),
    path('donor1/',views.Donor1.as_view(),name='donor1'),
    path('donor2/',views.Donor2.as_view(),name='donor2'),
]