from django.urls import path
from . import views

urlpatterns = [
    path('tr/', views.home, name='home'),
    path('tr/hakkimizda/', views.about, name='about'),
    path('tr/iletisim/', views.contact, name='contact'),
    path('tr/sss/', views.faq, name='faq'),
    path('tr/kvkk/', views.privacyPolicy, name='privacyPolicy'),
    path('tr/teklifal/', views.getOffer, name='getOffer'),

]
