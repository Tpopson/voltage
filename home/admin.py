from django.contrib import admin
from . models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','message','admin_note','status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','max','img','price','description','latest','featured','available']
    list_editable = ['img']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title','text','carousel']


admin.site.register(Contact,ContactAdmin)
admin.site.register(Product,ProductAdmin)


