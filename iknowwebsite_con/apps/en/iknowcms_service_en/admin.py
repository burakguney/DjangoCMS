from django.contrib import admin
from .models import Service
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"serviceSlug": ("serviceTitle",)}
    list_display = ('serviceTitle', 'serviceIcon', 'serviceSlug')
    search_fields = ('serviceTitle', )
    list_per_page = 15
