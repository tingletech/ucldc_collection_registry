from django.conf.urls import patterns, include, url
from dl_collections.feeds import AllFeed

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dl_collections.views.home', name='home'),
    url(r'rss$', AllFeed()),
    # Status/Format/Restriction/Need
    url(r'^(UC.*)/$', 'dl_collections.views.UC', name='UC'),
    #url(r'^(UC.*)/(Status)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Format)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Restriction)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Need)/(.*)$', 'dl_collections.views.UClimit', name='UClimit'),
    #url(r'^(?P<slug>.*)$', 'dl_collections.views.details', name='detail'),
    url(r'^(\d*)/(.*)/$', 'dl_collections.views.details', name='detail'),
    url(r'^(\d*)/$', 'dl_collections.views.details_by_id', name='detail'),
)
