# views.py

from django.shortcuts import render_to_response
from dl_collections.models import Collection
from django.shortcuts import get_object_or_404, get_list_or_404

def home(request):
    collections = Collection.objects.all().order_by('name')
    return render_to_response('dl_collections/index.html', { 'collections': collections })

def details(request, urlstuff):
    collection = get_object_or_404(Collection, slug=urlstuff)
    return render_to_response('dl_collections/collection.html', { 'collection': collection })


