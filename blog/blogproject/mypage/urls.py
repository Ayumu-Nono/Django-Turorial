from django.urls import path
from .views import MypageDataView
from . import views 

app_name='mypage'

urlpatterns = [
      path('', views.Top.as_view(), name='top'),
      # path('',MypageDataView.as_view(),name='mypage.data'), 
      path('login/',views.Login.as_view(),name='login'),
      path('logout/',views.Logout.as_view(),name='logout'),
]
