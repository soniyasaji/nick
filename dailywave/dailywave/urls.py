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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
app_name="newspaper"
app_name="magazines"
app_name="senior"
app_name="kids"
app_name="first"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('newspaper.urls')),
    path('senior/',include('senior.urls')),
    path('magazines/',include('magazines.urls')),
    path('kids/',include('kids.urls')),
    path('search/',include('search.urls')),
    path('cart/',include('cart.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)