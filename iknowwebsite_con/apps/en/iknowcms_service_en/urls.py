from django.urls import path
from . import views

urlpatterns = [
    path('', views.serviceList_en, name='serviceList_en'),
    path('<slug:serviceSlug>/', views.serviceSingle_en, name='serviceSingle_en'),
    path('partial/servicepartial/',
         views.servicePartial_en, name='servicePartial_en'),
]
