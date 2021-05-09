from django.urls import path
from . import views

urlpatterns = [
    path('', views.careerList_en, name='careerList_en'),
    path('<slug:careerSlug>/<int:pk>/',
         views.careerSingle_en, name='careerSingle_en')

]
