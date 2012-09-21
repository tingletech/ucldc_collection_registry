import sys,os
import os.path
import csv

from human_to_bytes import human2bytes

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))

csv_filepathname = os.path.join(pathname, "refine.tsv")
os.environ['DJANGO_SETTINGS_MODULE'] = 'collection_registry.settings'

from dl_collections.models import *

dataReader = csv.reader(open(csv_filepathname), delimiter='\t')

for row in dataReader:
    if row[0] != 'File': # Ignore the header row, import everything else
        collection = Collection()
        collection.name = row[2]
        collection.description = row[3]
        collection.url_local = row[6]
        if row[7]:
            collection.extent = int(human2bytes(row[7]))
        collection.hosted = row[8]
        collection.metadata_standard = row[10]
        collection.metadata_level = row[11]
        # collection.ready_for_surfacing
        collection.save()

        collection.campus.add(Campus.objects.get(slug = row[1]))
        if row[4]:
            collection.status.add(Status.objects.get(name = row[4]))
        # if row[]:
        #     collection.format.add(Format.objects.get(name = row[]))
        if row[9]:
            collection.need_for_dams.add(Need.objects.get(name = row[9]))
