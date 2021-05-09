from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolioList, name='portfolioList'),
    path('<slug:portfolioSlug>/', views.portfolioSingle, name='portfolioSingle'),
    path('partial/portfoliopartial/',
         views.portfolioPartial, name='portfolioPartial'),
]
