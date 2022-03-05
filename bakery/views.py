from django.shortcuts import render
from .models import *

# Create your views here.
def bakery_menu(request):
    cakelist = Cake.objects.all()
    biscuitlist = Biscuit.objects.all()
    ctx = {
        'cakelist':cakelist,
        'biscuitlist':biscuitlist,
    }
    return render(request,'menu.html',context=ctx)