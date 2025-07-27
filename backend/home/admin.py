from .models import Products_detail,Tag,Order,Setting
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
admin.site.unregister(User)
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
        "gettags"
    )
    list_display_links = ('product_name',)
    readonly_fields = ('adding_date', 'last_update', 'like_quantity')
    search_fields = ('product_name',)
    list_filter = ('adding_date',)
    ordering = ('-adding_date',)


@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    list_display=("user_name","orders_items","orders_quantity","order_add_time")
    readonly_fields=("order_add_time",)
    list_display_links=("user_name",)
    list_filter=("user_name",)
    ordering=("-order_add_time",)
@admin.register(Tag)
class tag_admin(admin.ModelAdmin):
    list_display=("tag_name","tag_author","tag_add_time")
    readonly_fields=("tag_add_time",)
    list_display_links=("tag_name",)
    list_filter=("tag_author",)
    ordering=("-tag_add_time",)

@admin.register(Setting)
class tag_admin(admin.ModelAdmin):
    list_display=("user","theme","language","privacy","setting_add_time")
    readonly_fields=("setting_add_time",)
    list_display_links=("user",)
    list_filter=("language",)
    ordering=("-setting_add_time",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'get_language',
        'order_count',
        'get_tags',
    )

    def get_language(self, obj):
        setting = Setting.objects.filter(user=obj).first()
        return setting.language if setting else "N/A"
    get_language.short_description = "Language"

    def order_count(self, obj):
        return Order.objects.filter(user_name=obj).count()
    order_count.short_description = "Total Orders"

    def get_tags(self, obj):
        tags = Tag.objects.filter(tag_author=obj)
        return ", ".join(tag.tag_name for tag in tags)
    get_tags.short_description = "Tags"
