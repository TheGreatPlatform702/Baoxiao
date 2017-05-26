from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from statistic import views as statistic_views

urlpatterns = patterns('',
    url(
        r'^$',
        statistic_views.home
    ),
)