from django.urls import path
from .views import *

urlpatterns = [
    path('', bakery_menu, name='bakery_menu'),
]