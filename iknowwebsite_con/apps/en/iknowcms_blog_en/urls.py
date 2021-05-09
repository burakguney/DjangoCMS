from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList_en, name='blogList_en'),
    path('<slug:blogSlug>/', views.BlogDetailView_en.as_view(), name='blogSingle_en'),
    path('partial/blogpartial/', views.blogPartial_en, name='blogPartial_en'),
]
