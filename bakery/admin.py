from django.contrib import admin
from .models import *
# Register your models here.
# adminview shortcut for registering models

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name','price','created_on')

@admin.register(Biscuit)
class Admin(admin.ModelAdmin):
    list_display = ('name','taste','price','created_on')
