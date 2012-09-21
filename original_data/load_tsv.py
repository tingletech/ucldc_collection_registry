import sys,os
import os.path
import csv

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
        collection.url = row[6]
        # collection.extent = row[7]
        collection.hosted = row[8]
        collection.metadata_standard = row[10]
        collection.metadata_level = row[11]
        collection.save()
