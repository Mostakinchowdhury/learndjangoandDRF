from .models import Blogs,Comment
from django.contrib import admin

@admin.register(Blogs)
class Blogsadmin(admin.ModelAdmin):
    list_display = (
       'blog_owner',
        'blog_text',
        'blog_img',
        'blog_upload_time',
        'blog_last_upload_time',
    )
    list_display_links = ('blog_owner',)
    readonly_fields = ('blog_upload_time', 'blog_last_upload_time')
    search_fields = ('blog_owner',)
    list_filter = ('blog_upload_time',)
    ordering = ('-blog_last_upload_time',)

@admin.register(Comment)
class comentadmin(admin.ModelAdmin):
    list_display = (
       'blog',
        'coment_text',
        'coment_date',
    )
    list_display_links=("blog",)
    search_fields = ('coment_text',)
    ordering=('-coment_date',)
