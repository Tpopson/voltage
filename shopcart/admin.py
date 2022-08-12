from django.contrib import admin
from . models import ShopCart
# Register your models here.

@admin.register(ShopCart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id','user','session_id', 'product','item_price','quantity','amount','order_code','order_placed']