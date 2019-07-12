from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView


app_name='donors'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='top.html'),name='top'),
    path('donors/',include('donors.urls')),
]
