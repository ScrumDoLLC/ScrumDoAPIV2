from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'api_example.views.home', name='home'),
    url(r'^oauth_callback$', 'api_example.views.oauth_callback', name='oauth_callback'),
    url(r'^organization/(?P<organization_slug>[-\w]+)$', 'api_example.views.project_list', name='project_list'),    
    url(r'^logout$', 'api_example.views.logout', name='logout'),    
) 

urlpatterns += staticfiles_urlpatterns()