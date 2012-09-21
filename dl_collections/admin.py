from django.contrib import admin
from dl_collections.models import Collection

class CollectionAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'extent', 'hosted',  )
    list_filter = ['campus', 'access_restrictions', 'status', 'need_for_dams', 'ready_for_surfacing']

admin.site.register(Collection, CollectionAdmin)
