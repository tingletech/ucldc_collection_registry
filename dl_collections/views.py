# views.py

from django.shortcuts import render_to_response
from dl_collections.models import Collection, Campus
from django.shortcuts import get_object_or_404, get_list_or_404
from human_to_bytes import bytes2human
from django.db.models import Sum

def home(request):
    collections = Collection.objects.all().order_by('name')
    raw_extent = Collection.objects.all().aggregate(Sum('extent'))['extent__sum']
    extent = bytes2human( raw_extent )
    return render_to_response('dl_collections/index.html', { 'collections': collections, 'extent':extent, })

def details(request, urlstuff):
    collection = get_object_or_404(Collection, slug=urlstuff)
    return render_to_response('dl_collections/collection.html', { 'collection': collection })

def UC(request, urlstuff):
    campus = get_object_or_404(Campus, slug=urlstuff)
    extent = bytes2human( Collection.objects.filter(campus__slug__exact=urlstuff).aggregate(Sum('extent'))['extent__sum'] or 0)
    collections = Collection.objects.filter(campus__slug__exact=urlstuff).order_by('name')
    return render_to_response('dl_collections/campus.html', { 'campus': campus, 'collections': collections, 'extent':extent, })


