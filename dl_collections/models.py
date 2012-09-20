from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=255)			#

class Status(models.Model):
    name = models.CharField(max_length=255)			#

class Format(models.Model):
    name = models.CharField(max_length=255)			#

class Restriction(models.Model):
    name = models.CharField(max_length=255)			#

class Level(models.Model):
    name = models.CharField(max_length=255)			#

class Standard(models.Model):
    name = models.CharField(max_length=255)			#

class Need(models.Model):
    name = models.CharField(max_length=255)			#

class Collection(models.Model):
    name = models.CharField(max_length=255)			#
    campus = models.ManyToManyField(Campus)	# why not a multi-campus collection?
    description = models.TextField()
    url_local = models.CharField(max_length=255)
    url_oac = models.CharField(max_length=255)
    url_was = models.CharField(max_length=255)
    status = models.ManyToManyField(Status)
    format = models.ManyToManyField(Format)
    extent = models.BigIntegerField(max_length=255)
    access_restrictions = models.ManyToManyField(Restriction)
    metadata_level = models.ManyToManyField(Level)
    metadata_standard = models.ManyToManyField(Standard)
    need_for_dams = models.ManyToManyField(Need)
    ready_for_surfacing = models.BooleanField()

