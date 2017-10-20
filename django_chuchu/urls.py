"""django_chuchu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^index1/', views.index1),
    url(r'^index2/', views.index2),
    url(r'^photo/', views.photo),
    url(r'^video/', views.video),
    url(r'^content/', views.content),
    url(r'^getvideo/', views.getvideo),
    url(r'^top_fixed/', views.top_fixed,name='top_fixed'),
    url(r'^ceshi_photo/', views.ceshi_photo),
    url(r'^delete/', views.delete_photo_model),
]
