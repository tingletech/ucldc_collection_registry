from django.db import models
from django_extensions.db.fields import AutoSlugField
from human_to_bytes import bytes2human


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
    # uuid_field = UUIDField(primary_key=True)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('name','description'))
    campus = models.ManyToManyField(Campus)	# why not a multi-campus collection?
    description = models.TextField(blank=True)
    url_local = models.CharField(max_length=255,blank=True)
    url_oac = models.CharField(max_length=255,blank=True)
    url_was = models.CharField(max_length=255,blank=True)
    hosted = models.CharField(max_length=255,blank=True)
    status = models.ManyToManyField(Status)
    format = models.ManyToManyField(Format)
    extent = models.BigIntegerField(blank=True, null=True)
    access_restrictions = models.ManyToManyField(Restriction)
    metadata_level = models.CharField(max_length=255,blank=True)
    metadata_standard = models.CharField(max_length=255,blank=True)
    need_for_dams = models.ManyToManyField(Need)
    ready_for_surfacing = models.BooleanField()

    def url(self):
        return self.url_local;

    def human_extent(self):
        return bytes2human(self.extent)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('', (), {
            'slug': self.slug,
        })

