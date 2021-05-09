from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolioList_en, name='portfolioList_en'),
    path('<slug:portfolioSlug>/', views.portfolioSingle_en,
         name='portfolioSingle_en'),
    path('partial/portfoliopartial/',
         views.portfolioPartial_en, name='portfolioPartial_en'),
]
