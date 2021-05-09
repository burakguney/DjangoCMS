from django.contrib import admin
from .models import About, Faq, PrivacyPolicy, Contact
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('aboutTitle',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contactTitle',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    prepopulated_fields = {"faqSlug": ("faqTitle",)}
    list_display = ('faqTitle', 'faqContent')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('policyTitle',)
