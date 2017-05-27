from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from bills import views as bills_views

urlpatterns = patterns('',
    url(
        r'^/list$',
        bills_views.showList
    ),
    url(
        r'^/create$',
        bills_views.create
    ),
    url(
        r'^/modify/(?P<bid>\d+)$', 
        bills_views.modify, 
        name='detail_table'
    )
)