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
from cart import views

app_name="cart"

urlpatterns = [
    path('add/<t>', views.add_to_cart, name="add_to_cart"),
    path('cart_view', views.cart_view, name="cart_view"),
    path('cart_remove/<t>',views.cart_remove,name="cart_remove"),
    path('full_remove/<t>', views.full_remove, name="full_remove"),
    path('order_form', views.order_form, name="order_form"),
    path('order_confirm', views.order_confirm, name="order_confirm"),
    path('orderview', views.orderview, name="orderview"),
]
