from django.contrib import admin
from .models import Blog, IpModel
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"blogSlug": ("blogTitle",)}
    list_display = ('blogTitle', 'blogImage', 'blogSlug', 'blogDate')
    search_fields = ('blogTitle', )
    list_filter = ('blogDate', )
    list_per_page = 15


@admin.register(IpModel)
class IpModelAdmin(admin.ModelAdmin):
    list_display = ('ip', 'date')
    list_filter = ('date', )
