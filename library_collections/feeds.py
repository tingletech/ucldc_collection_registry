from django.contrib.syndication.views import Feed
from library_collections.models import ProvenancialCollection

class AllFeed(Feed):
    title = "ucdlc rss feed"
    link = "/"
    def items(self):
        return ProvenancialCollection.objects.all()[:30]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description
