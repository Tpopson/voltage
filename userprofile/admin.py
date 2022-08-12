from cProfile import Profile
from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','email','phone','address','state','pix']
