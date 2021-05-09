from django.contrib import admin
from .models import Carousel, Testimonial, Client

# Register your models here.


@admin.register(Carousel)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('carouselTitle',)
    prepopulated_fields = {"carouselSlug": ("carouselTitle",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('testimonialTitle', 'testimonialImage')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientTitle', 'clientImage')
