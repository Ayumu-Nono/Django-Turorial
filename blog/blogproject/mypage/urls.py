from django.urls import path

from .views import MypageDataView

urlpatterns = [
      path('',MypageDataView.as_view(),name='mypage.data') # mypage/に飛んできた時にどこにいくか 
]
