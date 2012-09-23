from django.conf.urls import patterns, include, url
from dl_collections.models import Collection, Campus
#from dl_collections.sitemap import RegistrySitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
from django.contrib.sitemaps import GenericSitemap
from django.views.generic.simple import redirect_to
admin.autodiscover()


collection_dict = {
    'queryset': Collection.objects.all(),
}

campus_dict = {
    'queryset': Campus.objects.all(),
}

sitemaps = {
    "UC": GenericSitemap(campus_dict),
    "collection_registry": GenericSitemap(collection_dict),
}


urlpatterns = patterns('',
    # include the lookup urls
    (r'^admin/lookups/', include(ajax_select_urls)),

    # Examples:
    # url(r'^$', 'collection_registry.views.home', name='home'),
    url(r'^$', redirect_to, {'url': '/collection_registry/'}),
    url(r'^collection_registry/', include('dl_collections.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='sitemap')

)
