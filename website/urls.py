"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cliente import views

urlpatterns = [
    url(r'^$', views.home, name= 'cliente_home'),
    url(r'^cliente/$', views.cliente_lista, name= 'cliente_lista'),
    url(r'^cliente_novo/$', views.cliente_create, name= 'cliente_create'),
    url(r'^cliente/(?P<pk>\d+)/$', views.cliente_update, name= 'cliente_update'),
    url(r'^cliente_delete/(?P<pk>\d+)/$', views.cliente_delete, name= 'cliente_delete'),
    url(r'^admin/', include(admin.site.urls)),
]
