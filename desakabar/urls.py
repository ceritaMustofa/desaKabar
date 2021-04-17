"""desakabar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import frontpage
from apps.blog.views import indexBerita, post_detail, category_detail
from apps.profiledesa.views import indexProfileDesa, profileDesa_details 
from apps.statistikdesa.views import statistik_penduduk

#Django admin customization
admin.site.site_header = "Admin Desa Kabar"
admin.site.site_title = "Admin Desa Kabar"
admin.site.index_title = "Desa Kabar"

urlpatterns = [
    path('', frontpage, name='home'),
    path('blog/', indexBerita, name='indexBerita'),
    path('statistik/', statistik_penduduk, name='statistik_penduduk'),
    path('profile-desa/', indexProfileDesa, name='indexProfileDesa'), 
    path('admin/', admin.site.urls),


    #blog
    path('<slug:category_slug>/<slug:slug>/', post_detail, name='post_details'),
    path('<slug:slug>/', category_detail, name='category_details'),

    #profile desa
    path('<str:title>/', profileDesa_details, name='profileDesa_details'),    

    #ckedior
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
