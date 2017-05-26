from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FootballEventManagement.views.home', name='home'),
    # url(r'^FootballEventManagement/', include('FootballEventManagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(
    	r'^admin/',
    	include(admin.site.urls)
    ),
    url(
        r'^',
        include('registration.urls')
    ),
    url(
        r'^baoxiao',
        include('bills.urls')
    ),
    url(
        r'^statistic',
        include('statistic.urls')
    )
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),)