from django.contrib import admin
from .models import Portfolio
# Register your models here.


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"portfolioSlug": ("portfolioTitle",)}
    list_display = ('portfolioTitle', 'portfolioImage', 'portfolioSlug')
    search_fields = ('portfolioTitle', )
    list_per_page = 15
