from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
