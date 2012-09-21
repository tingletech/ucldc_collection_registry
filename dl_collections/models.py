from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=4)
    class Meta:
        verbose_name_plural = "campuses"
    def __unicode__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "statuses"
    def __unicode__(self):
        return self.name

class Format(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Restriction(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Need(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=255)
    campus = models.ManyToManyField(Campus)	# why not a multi-campus collection?
    description = models.TextField()
    url_local = models.CharField(max_length=255)
    url_oac = models.CharField(max_length=255)
    url_was = models.CharField(max_length=255)
    status = models.ManyToManyField(Status)
    format = models.ManyToManyField(Format)
    extent = models.BigIntegerField()
    access_restrictions = models.ManyToManyField(Restriction)
    metadata_level = models.CharField(max_length=255)
    metadata_standard = models.CharField(max_length=255)
    need_for_dams = models.ManyToManyField(Need)
    ready_for_surfacing = models.BooleanField()
    def __unicode__(self):
        return self.name

