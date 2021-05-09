"""iknowcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "iKnow CMS Admin Panel"
admin.site.site_title = "iKnow"
admin.site.site_url = None


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.tr.iknowcms_pages.urls')),
    path('tr/', include('apps.tr.iknowcms_partials.urls')),
    path('tr/blog/', include('apps.tr.iknowcms_blog.urls')),
    path('tr/projeler/', include('apps.tr.iknowcms_portfolio.urls')),
    path('tr/hizmetler/', include('apps.tr.iknowcms_service.urls')),
    path('tr/kariyer/', include('apps.tr.iknowcms_career.urls')),
    path('en/', include('apps.en.iknowcms_pages_en.urls')),
    path('en/', include('apps.en.iknowcms_partials_en.urls')),
    path('en/blog/', include('apps.en.iknowcms_blog_en.urls')),
    path('en/projects/', include('apps.en.iknowcms_portfolio_en.urls')),
    path('en/services/', include('apps.en.iknowcms_service_en.urls')),
    path('en/career/', include('apps.en.iknowcms_career_en.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

)
