from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList, name='blogList'),
    path('<slug:blogSlug>/', views.BlogDetailView.as_view(), name='blogSingle'),
    path('partial/blogpartial/', views.blogPartial, name='blogPartial'),
]
