# admin.py

from django.contrib import admin
from dl_collections.models import *
from django.contrib.sites.models import Site
 
class CollectionAdmin(admin.ModelAdmin):
    # http://stackoverflow.com/a/11321942/1763984
    def get_need_for_dams(self):
        return ", " . join([x.__str__() for x in self.need_for_dams.all()])
    def campuses(self):
        return ", " . join([x.__str__() for x in self.campus.all()])

    #readonly_fields=('slug',)
    list_display = ( 'name', campuses, 'extent', 'hosted', get_need_for_dams, 'metadata_level',)
    #list_display = ( 'name', campuses, 'extent', 'hosted', get_need_for_dams, 'ready_for_surfacing', 'metadata_level','access_mode',)
    list_filter = ['campus', 'access_restrictions', 'status', 'need_for_dams', 'ready_for_surfacing', 'access_mode',]
    #filter_vertical = ['status', 'format', 'access_restrictions', 'need_for_dams' ]
    search_fields = ['name','description']

class CampusAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Status)
admin.site.register(Format)
admin.site.register(Restriction)
admin.site.register(Need)
# http://stackoverflow.com/questions/5742279/removing-sites-from-django-admin-page
admin.site.unregister(Site)

