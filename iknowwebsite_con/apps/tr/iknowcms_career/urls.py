from django.urls import path
from . import views

urlpatterns = [
    path('', views.careerList, name='careerList'),
    path('<slug:careerSlug>/<int:pk>/', views.careerSingle, name='careerSingle')
]
