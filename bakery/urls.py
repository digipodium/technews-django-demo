from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', bakery_menu, name='bakery_menu'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('news', TemplateView.as_view(template_name='news.html'), name='news'),
]