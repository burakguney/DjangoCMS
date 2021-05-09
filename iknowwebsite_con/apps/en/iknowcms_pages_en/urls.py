from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_en, name='home_en'),
    path('about/', views.about_en, name='about_en'),
    path('contact/', views.contact_en, name='contact_en'),
    path('faq/', views.faq_en, name='faq_en'),
    path('privacypolicy/', views.privacyPolicy_en, name='privacyPolicy_en'),
    path('getoffer/', views.getOffer_en, name='getOffer_en'),

]
