from django.conf.urls import patterns, include, url
from provenancial_collections.feeds import AllFeed

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'provenancial_collections.views.home', name='home'),
    url(r'rss$', AllFeed()),
    # Status/Format/Restriction/Need
    url(r'^(UC.*)/$', 'provenancial_collections.views.UC', name='UC'),
    #url(r'^(UC.*)/(Status)/(.*)$', 'provenancial_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Format)/(.*)$', 'provenancial_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Restriction)/(.*)$', 'provenancial_collections.views.UClimit', name='UClimit'),
    #url(r'^(UC.*)/(Need)/(.*)$', 'provenancial_collections.views.UClimit', name='UClimit'),
    #url(r'^(?P<slug>.*)$', 'provenancial_collections.views.details', name='detail'),
    url(r'^(\d*)/(.*)/$', 'provenancial_collections.views.details', name='detail'),
    url(r'^(\d*)/$', 'provenancial_collections.views.details_by_id', name='detail'),
)
