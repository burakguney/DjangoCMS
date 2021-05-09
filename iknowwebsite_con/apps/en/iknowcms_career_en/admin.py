from django.contrib import admin
from .models import Career
# Register your models here.


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'careerSlug': ('careerTitle',)}
    list_display = ('careerTitle', 'careerDate')
    search_fields = ('careerTitle',)
    list_per_page = 15
