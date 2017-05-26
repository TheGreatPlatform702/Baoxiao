from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from bills import views as bills_views

urlpatterns = patterns('',
    url(
        r'^$',
        bills_views.home
    ),
)