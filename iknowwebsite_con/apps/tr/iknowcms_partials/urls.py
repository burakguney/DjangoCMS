from django.urls import path
from . import views

urlpatterns = [
    path('partial/carouselpartial/',
         views.carouselPartial, name='carouselPartial'),
    path('carousel/<slug:carouselSlug>/',
         views.carouselSingle, name='carouselSingle'),
    path('partial/testimonialpartial/',
         views.testimonialPartial, name='testimonialPartial'),
    path('partial/clientpartial/',
         views.clientPartial, name='clientPartial'),
    path('partial/footerpartial/',
         views.footerPartial, name='footerPartial'),

]
