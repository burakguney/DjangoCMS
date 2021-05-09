from django.urls import path
from . import views

urlpatterns = [
    path('', views.serviceList, name='serviceList'),
    path('<slug:serviceSlug>/', views.serviceSingle, name='serviceSingle'),
    path('partial/servicepartial/',
         views.servicePartial, name='servicePartial'),
]
