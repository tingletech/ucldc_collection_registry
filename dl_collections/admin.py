# admin.py

from django.contrib import admin
from dl_collections.models import *
 
class CollectionAdmin(admin.ModelAdmin):
    #readonly_fields=('slug',)
    list_display = ( 'name', 'extent', 'hosted',  )
    list_filter = ['campus', 'access_restrictions', 'status', 'need_for_dams', 'ready_for_surfacing']
    filter_vertical = ['campus', 'status', 'format', 'access_restrictions', 'need_for_dams']
    search_fields = ['name','description']

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Campus)
admin.site.register(Status)
admin.site.register(Format)
admin.site.register(Restriction)
admin.site.register(Need)
