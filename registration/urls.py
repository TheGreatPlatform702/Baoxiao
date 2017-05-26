from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from registration import views as registration_views

urlpatterns = patterns('',
    url(
        r'^$',
        registration_views.home
    ),
    url(
        r'^login$',
        registration_views.login
    ),
    url(
        r'^register$',
        registration_views.register
    ),
    url(
        r'^logout$',
        registration_views.logout
    )
)