from django.urls import path
from . import views

urlpatterns = [
    path('partial/carouselpartial/',
         views.carouselPartial_en, name='carouselPartial_en'),
    path('carousel/<slug:carouselSlug>/',
         views.carouselSingle_en, name='carouselSingle_en'),
    path('partial/testimonialpartial/',
         views.testimonialPartial_en, name='testimonialPartial_en'),
    path('partial/clientpartial/',
         views.clientPartial_en, name='clientPartial_en'),
    path('partial/footerpartial/',
         views.footerPartial_en, name='footerPartial_en'),

]
