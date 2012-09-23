from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dl_collections.views.home', name='home'),
    #url(r'^(?P<slug>.*)$', 'dl_collections.views.details', name='detail'),
    url(r'^(.*)$', 'dl_collections.views.details', name='detail'),
)
