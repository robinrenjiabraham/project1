"""myweb URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from .views import displayProduct, myProducts, addToCart, viewCart,writeCookie,readCookie,getData,getDataPage
from .classview import MyView


de
urlpatterns = [
    path ('pppp/<str:id>', displayProduct),
    path ('products', myProducts),
    path ('addToCart', addToCart),
    path ('viewCart', viewCart),
    path('writeCookie', writeCookie),
    path('readCookie', readCookie),
    path ('myview', MyView.as_view()),
    path ('productdata',getData),
    path ('data',getDataPage)
]