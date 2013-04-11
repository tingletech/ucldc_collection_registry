# admin.py

from django.contrib import admin
from dl_collections.models import *
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
 
class CollectionAdmin(admin.ModelAdmin):
    # http://stackoverflow.com/a/11321942/1763984
    def campuses(self):
        return ", " . join([x.__str__() for x in self.campus.all()])

    #def human_extent(self):
    #    return ""

    #readonly_fields=('slug',)
    list_display = ( 'name', campuses, 'human_extent', 'access_restrictions', 'access_mode',)
    list_editable = ( 'access_mode',)
    #list_display = ( 'name', campuses, 'extent', 'hosted', get_need_for_dams, 'ready_for_surfacing', 'metadata_level','access_mode',)
    list_filter = [ 'appendix','campus','need_for_dams','ready_for_surfacing',]
    #filter_vertical = ['status', 'format', 'access_restrictions', 'need_for_dams' ]
    search_fields = ['name','description']

class CampusAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Status)
admin.site.register(Restriction)
#admin.site.register(Need)
# http://stackoverflow.com/questions/5742279/removing-sites-from-django-admin-page

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
