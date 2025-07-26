from .models import Products_detail
from django.contrib import admin
@admin.register(Products_detail)
class Productadmin(admin.ModelAdmin):
    list_display = (
       'product_name',
        'product_price',
        'product_type',
        'product_description',
        'adding_date',
        'last_update',
        'like_quantity',
    )
    list_display_links = ('product_name',) 
    readonly_fields = ('adding_date', 'last_update', 'like_quantity')
    search_fields = ('product_name',)
    list_filter = ('adding_date',)
    ordering = ('-adding_date',)
