"""
URL configuration for dailywave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.first, name='first')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='first')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newspaper import views
from django.conf import settings
from django.conf.urls.static import static
app_name="newspaper"

from newspaper.views import videos,upload

urlpatterns = [
    path('admin',admin.site.urls),
    path('',views.home,name="first"),
    path('addnews',views.addnews,name="addnews"),
    path('viewnews',views.viewnews,name="viewnews"),
    path('newscategory',views.newscategory,name="newscategory"),
    path('newstype/<news>', views.newstype, name="newstype"),
    path('newsdetails/<t>',views.newsdetails,name="newsdetails"),
    path('register', views.register, name="register"),
    path('user_login', views.user_login, name="login"),
    path('user_logout', views.user_logout, name="logout"),
    path('videos',views.videos,name="videos"),
    path('upload/',views.upload,name="upload"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)